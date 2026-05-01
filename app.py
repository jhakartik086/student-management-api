from flask import Flask, jsonify, request
import sqlite3

# ---------------- DATABASE INIT ----------------
def init_db():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS student(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            s_class TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route('/')
def api():
    return 'API is Running'

# ---------------- ADD STUDENT ----------------
@app.route('/students/add', methods=['POST'])
def add():
    data = request.json

    if not data or 'name' not in data or 's_class' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    conn = sqlite3.connect('student.db')
    cur = conn.cursor()

    cur.execute('''
        INSERT INTO student(name, s_class)
        VALUES (?, ?)
    ''', (data['name'], data['s_class']))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Student added successfully'}), 201

# ---------------- DISPLAY ALL ----------------
@app.route('/students', methods=['GET'])
def display_all():
    conn = sqlite3.connect('student.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('SELECT * FROM student')
    rows = cur.fetchall()
    conn.close()

    students = [dict(row) for row in rows]
    return jsonify(students), 200

# ---------------- DISPLAY BY ID ----------------
@app.route('/students/<int:id>', methods=['GET'])
def display(id):
    conn = sqlite3.connect('student.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('SELECT * FROM student WHERE id = ?', (id,))
    row = cur.fetchone()
    conn.close()

    if row:
        return jsonify(dict(row)), 200
    else:
        return jsonify({'error': 'Student not found'}), 404

# ---------------- UPDATE ----------------
@app.route('/students/update', methods=['PUT'])
def update():
    data = request.json

    if not data or 'id' not in data or 'name' not in data or 's_class' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    conn = sqlite3.connect('student.db')
    cur = conn.cursor()

    cur.execute('''
        UPDATE student
        SET name = ?, s_class = ?
        WHERE id = ?
    ''', (data['name'], data['s_class'], data['id']))

    conn.commit()

    if cur.rowcount == 0:
        conn.close()
        return jsonify({'error': 'Student not found'}), 404

    conn.close()
    return jsonify({'message': 'Student updated successfully'}), 200

# ---------------- DELETE ----------------
@app.route('/students/delete/<int:id>', methods=['DELETE'])
def delete(id):
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()

    cur.execute('DELETE FROM student WHERE id = ?', (id,))
    conn.commit()

    if cur.rowcount == 0:
        conn.close()
        return jsonify({'error': 'Student not found'}), 404

    conn.close()
    return jsonify({'message': 'Student deleted successfully'}), 200

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)
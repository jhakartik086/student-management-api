from database.db import get_conn

def add_student(name,s_class):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute('''
        INSERT INTO student(name, s_class)
        VALUES (?, ?)
    ''', (name, s_class))

    conn.commit()
    conn.close()

def get_all_student():
    conn=get_conn()
    cur=conn.cursor()
    cur.execute('SELECT * FROM student')
    rows = cur.fetchall()
    conn.close()

    students = [dict(row) for row in rows]
    return students

def get_student_by_id(student_id):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute('SELECT * FROM student WHERE id = ?', (student_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None

def update_student(student_id,name,s_class):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute('''
        UPDATE student
        SET name = ?, s_class = ?
        WHERE id = ?
    ''', (name,s_class,student_id))
    row_count = cur.rowcount
    conn.commit()
    conn.close()
    return row_count
    
def delete_student(student_id):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute('DELETE FROM student WHERE id = ?', (student_id,))
    row_count = cur.rowcount
    conn.commit()
    conn.close()
    return row_count
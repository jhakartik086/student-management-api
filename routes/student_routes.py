from flask import Blueprint,jsonify,request
from models.student_model import *

student_bp = Blueprint('student',__name__)

@student_bp.route('/add',methods=['POST'])
def add():
    data = request.json

    if not data or 'name' not in data or 's_class' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    add_student(data['name'],data['s_class'])

    return jsonify({'message': 'Student added successfully'}), 201

@student_bp.route('/display',methods=['GET'])
def display_all():
    students=get_all_student()
    return jsonify(students), 200
    
@student_bp.route('/<int:id>',methods=['GET'])
def display_by_id(id):
    student = get_student_by_id(id)

    if not student:
        return jsonify({'error': 'Student not found'}), 404
    
    return jsonify(student)

@student_bp.route('/update',methods=['PUT'])
def update():
    data = request.json

    if not data or 'id' not in data or 'name' not in data or 's_class' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    count = update_student(data['id'],data['name'],data['s_class'])

    if count == 0:
        return jsonify({'error': 'Student not found'}), 404
    
    return jsonify({'message': 'Student updated successfully'}), 200

@student_bp.route('/delete/<int:id>',methods=['DELETE'])
def delete(id):
    count = delete_student(id)
    
    if count == 0:
        return jsonify({'error': 'Student not found'}), 404
    
    return jsonify({'message': 'Student deleted successfully'}), 200
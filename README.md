📘 Student CRUD API (Flask + SQLite)

A simple REST API built using Flask and SQLite to perform basic CRUD operations (Create, Read, Update, Delete) on student data.

🚀 Features ➕ Add a new student 📄 Get all students 🔍 Get student by ID ✏️ Update student details ❌ Delete a student 🛠️ Tech Stack Python 🐍 Flask 🌐 SQLite 🗄️ 📂 Project Structure project/ │ ├── app.py # Main Flask API ├── student.db # SQLite database (auto-created) └── README.md # Documentation ⚙️ Installation & Setup

Install dependencies pip install flask
Run the app python app.py
Server will start at: http://127.0.0.1:5000/ 📌 API Endpoints 🏠 Home GET /
Response:

API is Running ➕ Add Student POST /students/add Body (JSON): { "name": "Kartik", "s_class": "10" } 📄 Get All Students GET /students 🔍 Get Student by ID GET /students/

Example:

GET /students/1 ✏️ Update Student PUT /students/update Body (JSON): { "id": 1, "name": "Kartik Jha", "s_class": "10A" } ❌ Delete Student DELETE /students/delete/

Example:

DELETE /students/delete/1 🗄️ Database Schema Field Type Description id INTEGER Primary Key (Auto) name TEXT Student Name s_class TEXT Class of student ⚠️ Notes Database (student.db) is created automatically on first run Uses simple SQLite (no external DB needed) Returns JSON responses Proper HTTP status codes are used 💡 Future Improvements 🔐 Authentication (login system) 🔎 Search & filter students 📱 Connect with Android app 🌐 Frontend UI (HTML/CSS/JS) 👨‍💻 Author

Kartik Jha
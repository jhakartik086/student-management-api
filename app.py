from flask import Flask
from database.db import db_init
from routes.student_routes import student_bp

app = Flask(__name__)

#init db
db_init()

#register bp
app.register_blueprint(student_bp, url_prefix='/student')


if __name__ == '__main__':
    app.run(debug=True)
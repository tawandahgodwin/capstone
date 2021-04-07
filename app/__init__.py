from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import serial

from .models import Attendance


app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'



ser=serial.Serial('COM1',9600)
readedText = ser.readline()
print(readedText)
ser.close()


@app.route('/attendance_list')
def attendance_list():
    attendance_list = Attendance.query.all()
    return render_template(
        'attendance_list.html', 
        attendance_list = attendance_list
    )
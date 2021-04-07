import serial
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models

# Listen for RFID reader signals and write to the database
ser=serial.Serial('COM1',9600)
readedText = ser.readline()
print(readedText)
ser.close()


# Endpoint for viewing attendance list
@app.route('/attendance_list')
def attendance_list():
    attendance_list = Attendance.query.all()
    return render_template(
        'attendance_list.html', 
        attendance_list = attendance_list
    )
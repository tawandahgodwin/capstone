import datetime
from . import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg_number = db.Column(db.String(10), unique=True)
    rfid_tag = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now()))
    present = db.Column(db.Boolean)
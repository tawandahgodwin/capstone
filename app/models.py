import datetime
from . import db


attendances = db.Table('attendances',
    db.Column('attendance_id', db.Integer, db.ForeignKey('attendance.id'), primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True)
)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg_number = db.Column(db.String(10), unique=True)
    rfid_tag = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    attendances = db.relationship('Attendance', secondary=attendances, lazy='subquery',
        backref=db.backref('students', lazy=True))

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now())
    present = db.Column(db.Boolean)
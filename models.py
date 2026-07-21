from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
db = SQLAlchemy()



class User(UserMixin, db.Model):
    """User model for employees with accounts."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100))  # Consider storing hashed passwords
    email = db.Column(db.String(120), unique=True, nullable=False)
    time_entries = db.relationship('TimeEntry', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class TipEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    hours_worked = db.Column(db.Float, nullable=False)
    food_expense = db.Column(db.Float, nullable=False)
    cash_tips = db.Column(db.Float, nullable=False)
    credit_card_tips = db.Column(db.Float, nullable=False)
    total_tips = db.Column(db.Float, nullable=False)
class TimeCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    clock_in = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    clock_out = db.Column(db.DateTime, nullable=True)
    week_starting = db.Column(db.Date, nullable=False)  # Ensure this line is correct

    def __repr__(self):
        return f'<TimeCard {self.id} for User {self.user_id}>'
    
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)


class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    last_purchased = db.Column(db.Date, nullable=False)
    stock = db.Column(db.Integer, nullable=False)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.String(50), unique=True, nullable=False)

class TimePunch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    clock_in = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    clock_out = db.Column(db.DateTime)
    role = db.Column(db.String(50))
    employee = db.relationship('Employee', backref=db.backref('time_punches', lazy=True))


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    invoice_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500))

    member = db.relationship('Member', backref=db.backref('invoices', lazy=True))
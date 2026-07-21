import io
from operator import itemgetter
import colorama
from flask import Flask, flash, render_template, request, redirect, url_for, session, g
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from flask import Response
from flask import Flask, render_template, Response
from reportlab.pdfgen import canvas
from flask import Flask, render_template, request, redirect, url_for, session, g
from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from flask import request
from flask import Flask, render_template, request, jsonify
import PyPDF2
from flask import render_template, request, redirect, url_for, abort
from flask import request, redirect, url_for
from datetime import datetime
from flask import session
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import current_user, login_required
from flask_login import LoginManager
from flask_login import UserMixin
from flask import Flask
from models import db, User
from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models import User, db
from flask import send_file
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
import stripe
from flask import render_template, redirect, url_for, request
from order_form import OrderForm
from flask import render_template, request, redirect, url_for
from datetime import datetime
from flask import render_template
import pdfkit
from flask import Flask, render_template, request, make_response
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base
from reportlab.pdfgen import canvas
from flask import request, redirect
from flask import render_template, request, redirect, url_for, jsonify
from flask_login import current_user
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask import Flask
from flask import Flask
from flask_migrate import Migrate
import os
from flask import send_from_directory
from werkzeug.utils import secure_filename
import logging
import traceback
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_migrate import Migrate
import os
from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
from flask import Flask, request, redirect, url_for, render_template, session, flash, jsonify
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Employee, TimePunch
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os
from io import BytesIO
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from io import BytesIO
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os




app = Flask(__name__)
app.secret_key =  'sk_live'
 # Replace with your actual secret key
app.config['UPLOAD_FOLDER'] = 'path/to/your/upload/folder'  # Make sure this path exists
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Ensure this directory exists
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}
app.secret_key = 'supersecretkey'  # Replace with your secret key
app.config['ALLOWED_EXTENSIONS'] = {'csv'}


# Configure your SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


migrate = Migrate(app, db)  # Initialize Flask-Migrate
migrate = Migrate(app, db)
stripe.api_key = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'  # Adjust this URI to your actual database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to your secret key


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', 'ACbade209ca773f0f5a23ed7bf02010ad2')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', '5a5d866213763f3d62364caea90a38f5')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', '+18448037867')


















app = Flask(__name__)
app.secret_key = ''  # Replace with your actual secret key

def generate_pdf_receipt(order_data):
    # Create a unique filename for the PDF, e.g., using order_id or timestamp
    pdf_filename = f"order_receipt_{order_data['order_id']}.pdf"

    # Create a PDF document
    pdf_canvas = canvas.Canvas(pdf_filename)
    pdf_canvas.setTitle('Order Receipt')

    # Define content for the PDF (customize this as needed)
    order_id = order_data['order_id']
    customer_name = order_data['customer_name']
    total_price = order_data['total_price']

    # Add content to the PDF
    pdf_canvas.drawString(100, 750, f"Order Receipt - Order #{order_id}")
    pdf_canvas.drawString(100, 730, f"Customer: {customer_name}")
    pdf_canvas.drawString(100, 710, f"Total Price: ${total_price:.2f}")

    # Save the PDF to the server
    pdf_canvas.save()

    # Return the PDF as a response
    with open(pdf_filename, 'rb') as pdf_file:
        pdf_content = pdf_file.read()
    
    response = Response(pdf_content, content_type='application/pdf')
    response.headers['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
    
    return response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timecards.db'  # Use your actual database URI
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace 'your_secret_key' with your actual secret key
db.init_app(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    return f"Data received: {data}"




ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db




# Sample catalog data (you can replace this with your actual data)
catalog = [
    {"id": 1, "name": "Item 1", "price": 10.0},
    {"id": 2, "name": "Item 2", "price": 15.0},
    {"id": 3, "name": "Item 3", "price": 12.0},
]

cart = []




class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    orders = db.relationship('Order', backref='member', lazy=True)

    def __repr__(self):
        return f'<Member {self.first_name} {self.last_name}>'
with app.app_context():
    db.create_all() 


@app.route('/dashboard')
def dashboard():
    total_members = Member.query.count()
    return render_template('dashboard.html', total_members=total_members)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, title, start, end, description=None):
        self.title = title
        self.start = start
        self.end = end
        self.description = description

@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    if request.method == 'POST':
        title = request.form['title']
        start = datetime.fromisoformat(request.form['start'])
        end = datetime.fromisoformat(request.form['end'])
        description = request.form.get('description', 'N/A')
        new_event = Event(title=title, start=start, end=end, description=description)
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('calendar'))
    return render_template('calendar.html')



@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    events_list = [
        {
            "id": event.id,
            "title": event.title,
            "start": event.start.isoformat(),
            "end": event.end.isoformat(),
            "description": event.description
        }
        for event in events
    ]
    return jsonify(events_list)


@app.route('/edit_event/<int:event_id>', methods=['POST'])
def edit_event(event_id):
    event = Event.query.get(event_id)
    if event:
        event.title = request.form['title']
        event.start = datetime.fromisoformat(request.form['start'])
        event.end = datetime.fromisoformat(request.form['end'])
        event.description = request.form.get('description', 'N/A')
        db.session.commit()
    return redirect(url_for('calendar'))

@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    if event:
        db.session.delete(event)
        db.session.commit()
    return '', 204


class TipEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    hours_worked = db.Column(db.Float, nullable=False)
    food_expense = db.Column(db.Float, nullable=False)
    cash_tips = db.Column(db.Float, nullable=False)
    credit_card_tips = db.Column(db.Float, nullable=False)
    total_tips = db.Column(db.Float, nullable=False)

@app.route('/tip-entry', methods=['GET', 'POST'])
def tip_entry():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        data = request.get_json()
        date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        entries = []
        
        for entry in data['data']:
            total_tips = max(float(entry['cash_tips']) + float(entry['credit_card_tips']) - float(entry['food_expense']), 0)
            tip_entry = TipEntry(
                date=date,
                name=entry['name'],
                hours_worked=float(entry['hours']),
                food_expense=float(entry['food_expense']),
                cash_tips=float(entry['cash_tips']),
                credit_card_tips=float(entry['credit_card_tips']),
                total_tips=total_tips
            )
            entries.append(tip_entry)
        
        db.session.add_all(entries)
        db.session.commit()
        return jsonify({'success': True})

    return render_template('tip_entry.html')



@app.route('/get-tips', methods=['GET'])
def get_tips():
    date = request.args.get('date')
    tips = TipEntry.query.filter_by(date=datetime.strptime(date, '%Y-%m-%d').date()).all()
    tip_list = [
        {
            'name': tip.name,
            'hours': tip.hours_worked,
            'food_expense': tip.food_expense,
            'cash_tips': tip.cash_tips,
            'credit_card_tips': tip.credit_card_tips,
            'total_tips': tip.total_tips
        } for tip in tips
    ]
    return jsonify(tip_list)



@app.route('/tip-entry', methods=['POST'])
def save_tip_entries():
    data = request.json
    date = datetime.strptime(data['date'], '%Y-%m-%d').date()
    total_cash_tips = data['totalCashTips']
    total_credit_card_tips = data['totalCreditCardTips']
    entries = data['data']

    for entry in entries:
        tip_entry = TipEntry(
            date=date,
            name=entry['name'],
            hours_worked=float(entry['hours']),
            food_expense=float(entry['food_expense']),
            cash_tips=float(entry['cash_tips']),
            credit_card_tips=float(entry['credit_card_tips']),
            total_tips=float(entry['total_tips'])
        )
        db.session.add(tip_entry)

    db.session.commit()
    return jsonify({'success': True})

@app.route('/view-tips', methods=['GET'])
def view_tips():
    tips = db.session.query(TipEntry.date).distinct().all()
    return render_template('view_tips.html', dates=[tip.date for tip in tips])


@app.route('/get-saved-dates', methods=['GET'])
def get_saved_dates():
    dates = db.session.query(TipEntry.date).distinct().all()
    date_list = [date[0].strftime('%Y-%m-%d') for date in dates]
    return jsonify(date_list)





@app.route('/edit-tips/<date>', methods=['GET', 'POST'])
def edit_tips(date):
    selected_date = datetime.strptime(date, '%Y-%m-%d').date()
    tips = TipEntry.query.filter_by(date=selected_date).all()
    
    if request.method == 'POST':
        for tip in tips:
            tip.name = request.form[f'name_{tip.id}']
            tip.hours_worked = float(request.form[f'hours_worked_{tip.id}'])
            tip.food_expense = float(request.form[f'food_expense_{tip.id}'])
            tip.cash_tips = float(request.form[f'cash_tips_{tip.id}'])
            tip.credit_card_tips = float(request.form[f'credit_card_tips_{tip.id}'])
            tip.total_tips = max(tip.cash_tips + tip.credit_card_tips - tip.food_expense, 0)
        
        db.session.commit()
        return redirect(url_for('view_tips'))

    return render_template('edit_tips.html', selected_date=selected_date, tips=tips)

@app.route('/delete-tips/<date>', methods=['POST'])
def delete_tips(date):
    selected_date = datetime.strptime(date, '%Y-%m-%d').date()
    TipEntry.query.filter_by(date=selected_date).delete()
    db.session.commit()
    return redirect(url_for('view_tips'))



class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(50), nullable=False)
    table_number = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    x = db.Column(db.Integer, nullable=False)  # X coordinate on the map
    y = db.Column(db.Integer, nullable=False)  # Y coordinate on the map

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(150), nullable=False)
    reservation_time = db.Column(db.DateTime, nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)
    table = db.relationship('Table', backref=db.backref('reservations', lazy=True))



@app.route('/layout')
def layout():
    tables = Table.query.all()
    reservations = Reservation.query.filter(Reservation.reservation_time > datetime.now()).all()
    reserved_tables = {reservation.table_id: reservation for reservation in reservations}
    return render_template('layout.html', tables=tables, reserved_tables=reserved_tables)

@app.route('/reserve', methods=['POST'])
def reserve():
    customer_name = request.form['customer_name']
    reservation_time = request.form['reservation_time']
    table_id = request.form['table_id']
    reservation_time = datetime.strptime(reservation_time, '%Y-%m-%dT%H:%M')

    reservation = Reservation(customer_name=customer_name, reservation_time=reservation_time, table_id=table_id)
    db.session.add(reservation)
    db.session.commit()
    flash('Reservation made successfully!', 'success')
    return redirect(url_for('layout'))

@app.route('/admin')
def admin():
    reservations = Reservation.query.all()
    return render_template('admin.html', reservations=reservations)

@app.route('/edit_layout')
def edit_layout():
    tables = Table.query.all()
    return render_template('edit_layout.html', tables=tables)

@app.route('/add_table', methods=['POST'])
def add_table():
    section = request.form['section']
    table_number = request.form['table_number']
    seats = request.form['seats']
    x = request.form['x']
    y = request.form['y']
    table = Table(section=section, table_number=table_number, seats=seats, x=x, y=y)
    db.session.add(table)
    db.session.commit()
    flash('Table added successfully!', 'success')
    return redirect(url_for('edit_layout'))

@app.route('/delete_table/<int:table_id>')
def delete_table(table_id):
    table = Table.query.get_or_404(table_id)
    db.session.delete(table)
    db.session.commit()
    flash('Table deleted successfully!', 'success')
    return redirect(url_for('edit_layout'))

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phone_number = db.Column(db.String(50))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/customers', methods=['GET', 'POST'])
def customers():
    search_query = request.args.get('search')
    customers = []
    if search_query:
        customers = Customer.query.filter(
            (Customer.first_name.ilike(f'%{search_query}%')) |
            (Customer.last_name.ilike(f'%{search_query}%')) |
            (Customer.email.ilike(f'%{search_query}%'))
        ).all()
    else:
        customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        
        new_customer = Customer(
            first_name=first_name, 
            last_name=last_name, 
            email=email,
            phone_number=phone_number
        )
        
        db.session.add(new_customer)
        db.session.commit()
        flash('Customer added successfully!')
        return redirect(url_for('customers'))
    return render_template('add_customer.html')

@app.route('/edit_customer/<int:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    if request.method == 'POST':
        customer.first_name = request.form.get('first_name')
        customer.last_name = request.form.get('last_name')
        customer.email = request.form.get('email')
        customer.phone_number = request.form.get('phone_number')
        
        db.session.commit()
        flash('Customer updated successfully!')
        return redirect(url_for('customers'))
    return render_template('edit_customer.html', customer=customer)


@app.route('/delete_customer/<int:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    flash('Customer deleted successfully!')
    return redirect(url_for('customers'))

@app.route('/export_customers')
def export_customers():
    customers = Customer.query.all()
    customer_list = [{"ID": c.id, 
                      "First Name": c.first_name, 
                      "Last Name": c.last_name, 
                      "Email": c.email,
                      "Phone Number": c.phone_number} for c in customers]
    df = pd.DataFrame(customer_list)
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', download_name='customers.csv', as_attachment=True)



@app.route('/import_customers', methods=['GET', 'POST'])
def import_customers():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            try:
                df = pd.read_csv(file)
                added_count = 0
                for index, row in df.iterrows():
                    new_customer = Customer(
                        first_name=row['First Name'],
                        last_name=row['Last Name'],
                        email=row['Email'],
                        phone_number=row.get('Phone Number', '')
                    )
                    db.session.add(new_customer)
                    added_count += 1
                db.session.commit()
                flash(f'{added_count} customers imported successfully!', 'success')
            except KeyError as e:
                flash(f'CSV file is missing the required column: {e}', 'danger')
            except Exception as e:
                flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('customers'))
        else:
            flash('Invalid file format. Please upload a CSV file.', 'danger')
    return render_template('import_customers.html')

class Waitlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    notified = db.Column(db.Boolean, default=False)
    customer = db.relationship('Customer', backref=db.backref('waitlist_entries', lazy=True))



@app.route('/waitlist', methods=['GET', 'POST'])
def waitlist():
    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        new_entry = Waitlist(customer_id=customer_id)
        db.session.add(new_entry)
        db.session.commit()
        flash('Customer added to waitlist successfully!')
        return redirect(url_for('waitlist'))
    
    waitlist_entries = Waitlist.query.order_by(Waitlist.timestamp).all()
    customers = Customer.query.all()
    return render_template('waitlist.html', waitlist_entries=waitlist_entries, customers=customers)

@app.route('/notify/<int:waitlist_id>', methods=['POST'])
def notify(waitlist_id):
    entry = Waitlist.query.get_or_404(waitlist_id)
    customer = entry.customer
    entry.notified = True
    db.session.commit()
    message = f"Dear {customer.first_name}, your table is ready at The Draft Room! Please proceed to the host stand."
    send_sms(customer.phone_number, message)
    flash('Customer has been notified via SMS.')
    return redirect(url_for('waitlist'))



def send_sms(to, message):
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
    except Exception as e:
        print(f"Error sending SMS: {e}")



@app.route('/delete_waitlist_entry/<int:waitlist_id>', methods=['POST'])
def delete_waitlist_entry(waitlist_id):
    entry = Waitlist.query.get_or_404(waitlist_id)
    db.session.delete(entry)
    db.session.commit()
    flash('Customer removed from waitlist.')
    return redirect(url_for('waitlist'))



























class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    hourly_wage = db.Column(db.Float, nullable=False)
    ssn = db.Column(db.String(11), nullable=False)




@app.route('/employees')
def employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)



@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        position = request.form.get('position')
        hourly_wage = request.form.get('hourly_wage')
        ssn = request.form.get('ssn')
        new_employee = Employee(name=name, phone=phone, position=position, hourly_wage=hourly_wage, ssn=ssn)
        db.session.add(new_employee)
        db.session.commit()
        flash('Employee added successfully!', 'success')
        return redirect(url_for('employees'))
    return render_template('add_employee.html')

@app.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get_or_404(id)
    if request.method == 'POST':
        employee.name = request.form.get('name')
        employee.phone = request.form.get('phone')
        employee.position = request.form.get('position')
        employee.hourly_wage = request.form.get('hourly_wage')
        employee.ssn = request.form.get('ssn')
        try:
            db.session.commit()
            flash('Employee updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error updating employee: {}'.format(str(e)), 'danger')
        return redirect(url_for('employees'))
    return render_template('edit_employee.html', employee=employee)


@app.route('/delete_employee/<int:id>')
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    flash('Employee deleted successfully!', 'success')
    return redirect(url_for('employees'))


@app.route('/view_ssn/<int:id>')
def view_ssn(id):
    employee = Employee.query.get_or_404(id)
    return jsonify({'ssn': employee.ssn})



















@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')




















UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(150), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    role = db.Column(db.String(100), nullable=False)




# Route for adding a new member
@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        new_member = Member(first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_member)
        db.session.commit()
        flash('Member added successfully!')
        return redirect(url_for('members'))
    return render_template('add_member.html')


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        role = request.form['role']
        
        new_shift = Shift(
            employee_name=employee_name,
            date=datetime.strptime(date, '%Y-%m-%d').date(),
            start_time=datetime.strptime(start_time, '%H:%M').time(),
            end_time=datetime.strptime(end_time, '%H:%M').time(),
            role=role
        )
        db.session.add(new_shift)
        db.session.commit()
        flash('Shift scheduled successfully', 'success')
        return redirect(url_for('schedule'))
    
    shifts = Shift.query.all()
    return render_template('schedule.html', shifts=shifts)

@app.route('/edit_shift/<int:id>', methods=['GET', 'POST'])
def edit_shift(id):
    shift = Shift.query.get_or_404(id)
    if request.method == 'POST':
        shift.employee_name = request.form['employee_name']
        shift.date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        shift.start_time = datetime.strptime(request.form['start_time'], '%H:%M').time()
        shift.end_time = datetime.strptime(request.form['end_time'], '%H:%M').time()
        shift.role = request.form['role']
        db.session.commit()
        flash('Shift updated successfully', 'success')
        return redirect(url_for('schedule'))
    return render_template('edit_shift.html', shift=shift)

@app.route('/delete_shift/<int:id>')
def delete_shift(id):
    shift = Shift.query.get_or_404(id)
    db.session.delete(shift)
    db.session.commit()
    flash('Shift deleted successfully', 'success')
    return redirect(url_for('schedule'))

@app.route('/api/shifts')
def api_shifts():
    shifts = Shift.query.all()
    events = []
    for shift in shifts:
        events.append({
            'id': shift.id,
            'title': f"{shift.employee_name} ({shift.role})",
            'start': f"{shift.date}T{shift.start_time}",
            'end': f"{shift.date}T{shift.end_time}"
        })
    return jsonify(events)



# Dummy data for member profiles
member_profiles = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john@example.com", "phone": "123-456-7890", "membership_level": "Gold"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "email": "jane@example.com", "phone": "987-654-3210", "membership_level": "Silver"},
    # Add more member profiles here if needed
]

# Route for member profile page
@app.route('/member-profile/<int:member_id>')
def member_profile(member_id):
    member = Member.query.get_or_404(member_id)
    orders = Order.query.filter_by(member_id=member.id).all()
    notes = Note.query.filter_by(member_id=member.id).all()
    invoices = Invoice.query.filter_by(member_id=member.id).all()

    return render_template('member_profile.html', member=member, orders=orders, notes=notes, invoices=invoices)

# Sample data structure to store member information
members_data = [
    {
        'id': 1,
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'johndoe@example.com',
        'phone': '555-1234'
    },
    {
        'id': 2,
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'janesmith@example.com',
        'phone': '555-5678'
    }
]

# Route to edit a member
@app.route('/edit-member/<int:member_id>', methods=['GET', 'POST'])
def edit_member(member_id):
    member = Member.query.get_or_404(member_id)
    if request.method == 'POST':
        member.first_name = request.form['first_name']
        member.last_name = request.form['last_name']
        member.email = request.form['email']

        db.session.commit()
        return redirect(url_for('member_profile', member_id=member.id))

    return render_template('edit_member.html', member=member)


# Route to delete a member
@app.route('/delete_member/<int:member_id>', methods=['POST'])
def delete_member(member_id):
    member = Member.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('show_members_page'))

@app.route('/delete_members', methods=['POST'])
@app.route('/delete_members', methods=['POST'])
def delete_members():
    member_ids = request.form.getlist('member_ids')
    if member_ids:
        for member_id in member_ids:
            orders = Order.query.filter_by(member_id=member_id).all()
            for order in orders:
                db.session.delete(order)
            member = Member.query.get(member_id)
            if member:
                db.session.delete(member)
        db.session.commit()
        flash(f'Successfully deleted {len(member_ids)} members!', 'success')
    else:
        flash('No members selected for deletion', 'danger')
    return redirect(url_for('members'))

@app.route('/members', methods=['GET'])
def show_members_page():
    search_query = request.args.get('search', '')  # Get the search parameter from the URL
    if search_query:
        # Perform a case-insensitive search for first name, last name, or email
        members = Member.query.filter(
            db.or_(
                Member.first_name.ilike(f'%{search_query}%'),
                Member.last_name.ilike(f'%{search_query}%'),
                Member.email.ilike(f'%{search_query}%')
            )
        ).all()
    else:
        members = Member.query.all()
    return render_template('members.html', members=members)



# Route to display members list
@app.route('/members', methods=['GET', 'POST'])
def members():
    search_query = request.args.get('search')
    members = []
    if search_query:
        members = Member.query.filter(
            (Member.first_name.ilike(f'%{search_query}%')) |
            (Member.last_name.ilike(f'%{search_query}%')) |
            (Member.email.ilike(f'%{search_query}%'))
        ).all()
        db = get_db()
    username = session['username']
    user_data = db.execute('SELECT first_name FROM users WHERE username = ?', (username,)).fetchone()
    return render_template('members.html', members=members)




@app.route('/export_members')
def export_members():
    members = Member.query.all()
    member_list = [{"ID": m.id, "First Name": m.first_name, "Last Name": m.last_name, "Email": m.email} for m in members]
    df = pd.DataFrame(member_list)
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', download_name='members.csv', as_attachment=True)


@app.route('/import_members', methods=['GET', 'POST'])
def import_members():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            flash('No file selected', 'danger')
            return redirect(request.url)
        try:
            df = pd.read_csv(file)
            added_count = 0
            for index, row in df.iterrows():
                if 'First Name' in row and 'Last Name' in row and 'Email' in row:
                    new_member = Member(
                        first_name=row['First Name'],
                        last_name=row['Last Name'],
                        email=row['Email']
                    )
                    db.session.add(new_member)
                    added_count += 1
                else:
                    flash('CSV file is missing required columns', 'danger')
                    return redirect(request.url)
            db.session.commit()
            flash(f'{added_count} members imported successfully!', 'success')
        except KeyError as e:
            flash(f'CSV file is missing the required column: {e}', 'danger')
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
        return redirect(url_for('members'))
    return render_template('import_members.html')





@app.route('/create-checkout-session/<int:member_id>', methods=['GET'])
def create_checkout_session(member_id):
    member = Member.query.get_or_404(member_id)
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Membership Fee',
                        },
                        'unit_amount': 1000,  # Charge amount in cents
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=url_for('success', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('cancel', member_id=member_id, _external=True),
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return str(e)



@app.route('/success')
def success():
    session_id = request.args.get('session_id')
    # You can retrieve the session for more details or update member status here
    return render_template('success.html')

@app.route('/member/<int:member_id>/cancel')
def cancel(member_id):
    # Handle the cancellation
    return render_template('member_profile.html', member_id=member_id, message="Payment cancelled.")


# Define Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Order('{self.id}', '{self.member_id}', '{self.amount}', '{self.date}')"


# Create Order History Page
@app.route('/order-history/<int:member_id>')
def order_history(member_id):
    member = Member.query.get_or_404(member_id)
    orders = member.orders.order_by(Order.date.desc()).all()
    return render_template('order_history.html', member=member, orders=orders,)

@app.route('/members/<int:member_id>/add_order', methods=['POST'])
def add_order(member_id):
    if request.method == 'POST':
        amount = request.form['amount']
        # Validate and process the form data
        if amount:
            # Create a new order
            new_order = Order(amount=amount, date=datetime.now(), member_id=member_id)
            # Add the order to the database
            db.session.add(new_order)
            db.session.commit()
    return redirect(url_for('member_profile', member_id=member_id))


@app.route('/edit_order/<int:order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    order = Order.query.get_or_404(order_id)
    form = OrderForm()
    if form.validate_on_submit():
        order.amount = form.amount.data
        order.date = form.date.data
        db.session.commit()
        return redirect(url_for('member_profile', member_id=order.member_id))
    elif request.method == 'GET':
        form.amount.data = order.amount
        form.date.data = order.date
    return render_template('edit_order.html', form=form, order=order)

@app.route('/delete_order/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    flash('Order deleted successfully', 'success')
    return redirect(url_for('member_profile', member_id=order.member_id))


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    member = db.relationship('Member', backref=db.backref('notes', lazy=True))


@app.route('/member/<int:member_id>/add_note', methods=['POST'])
def add_note(member_id):
    if request.method == 'POST':
        member = Member.query.get_or_404(member_id)
        note_content = request.form['note_content']
        new_note = Note(content=note_content, member_id=member.id)
        db.session.add(new_note)
        db.session.commit()
    return redirect(url_for('member_profile', member_id=member_id))

@app.route('/member/<int:member_id>/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(member_id, note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST':
        note.content = request.form['note_content']
        db.session.commit()
        return redirect(url_for('member_profile', member_id=member_id))
    return render_template('edit_note.html', note=note)

@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted successfully', 'success')
    return redirect(url_for('member_profile', member_id=note.member_id))


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    member = db.relationship('Member', backref=db.backref('invoices', lazy=True))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload_invoice/<int:member_id>', methods=['POST'])
def upload_invoice(member_id):
    if 'invoice_pdf' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['invoice_pdf']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        db = get_db()
        db.execute('INSERT INTO invoices (member_id, filename) VALUES (?, ?)', (member_id, filename))
        db.commit()
        flash('Invoice successfully uploaded')
    return redirect(url_for('member_profile', member_id=member_id))




@app.route('/view_invoice/<int:invoice_id>')
def view_invoice(invoice_id):
    db = get_db()
    invoice = db.execute('SELECT * FROM invoices WHERE id = ?', (invoice_id,)).fetchone()
    if invoice is None:
        flash('Invoice not found')
        return redirect(url_for('members'))
    return send_from_directory(app.config['UPLOAD_FOLDER'], invoice['filename'])

@app.route('/invoice_maker', methods=['GET', 'POST'])
def invoice_maker():
    # Replace this logic with fetching member details from your database
    member = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'address': '123 Main Street, City, Country'
    }
    if request.method == 'POST':
        # Retrieve form data
        date = request.form['date']
        description = request.form['description']
        amount = request.form['amount']

        # Process the invoice creation (add to database, send email, etc.)
        # Redirect to a success page or render a success message
        return redirect(url_for('invoice_created'))

    return render_template('invoice_maker.html', member=member)

@app.route('/create_invoice', methods=['POST'])
def create_invoice():
    if request.method == 'POST':
        # Retrieve form data
        member_id = request.form['member_id']
        date = request.form['date']
        description = request.form['description']
        amount = request.form['amount']

        # Logic to create invoice and save to database
        # Redirect to a success page or render a success message
        return render_template('invoice_created.html')
    
@app.route('/invoice_created')
def invoice_created():
    return render_template('invoice_created.html')

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    if request.method == 'POST':
        # Get the member ID from the form
        member_id = request.form.get('member_id')
        
        # Fetch member details based on the member ID
        member_details = get_member_details(member_id)
        
        # Render the Invoice Maker page with member details
        return render_template('invoice_maker.html', member_details=member_details)

@app.route('/submit_invoice', methods=['POST'])
def submit_invoice():
    member_id = request.form['member_id']
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']

    # Fetch member data based on member_id
    member = fetch_member_from_database(member_id)

    # Create HTML content for the invoice
    html_content = render_template('invoice_template.html', member_id=member_id, date=date, description=description, amount=amount)

    # Generate PDF from HTML content
    pdf = pdfkit.from_string(html_content, False)

    # Send PDF as a file download
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=invoice.pdf'
    return response
def get_member_details(member_id):
    # Your database query to fetch member details based on the member ID goes here
    # For now, let's return some placeholder member details
    member_details = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'address': '123 Main Street, Anytown, USA',
        # Add more member details as needed
    }
    return member_details


# Function to fetch member details from the database
def fetch_member_from_database(member_id):
    # Implement your logic here to fetch member details from the database
    # This function should return the member details as a dictionary
    # For example:
    member_details = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'address': '123 Main Street, City, Country'
    }
    return member_details


@app.route('/')
def index():
    items = Item.query.all()
    return redirect(url_for('layout'))
    return render_template('index.html', pdf_data=pdf_data, items=items)

@app.route('/upload', methods=['POST'])
def upload():
    if 'pdf_file' in request.files:
        pdf_file = request.files['pdf_file']
        if pdf_file.filename != '':
            try:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                text = ''
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    text += page.extractText()

                pdf_data.append(text)
            except Exception as e:
                return "Error processing PDF: " + str(e)

    return redirect(url_for('index'))

@app.route('/place-order', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        # Process order submission
        product = request.form['product']
        quantity = request.form['quantity']
        # Save order details to database or perform other actions as needed

        # Redirect to the order confirmation page or any other page
        return render_template('order_confirmation.html', product=product, quantity=quantity)
    else:
        return render_template('place_order.html')

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_id = int(request.form['item_id'])
    item = next((x for x in catalog if x['id'] == item_id), None)
    if item:
        cart.append(item)
    return jsonify({"message": "Item added to cart successfully"})

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    item_id = int(request.form['item_id'])
    item = next((x for x in cart if x['id'] == item_id), None)
    if item:
        cart.remove(item)
    return jsonify({"message": "Item removed from cart successfully"})



DATABASE = 'application.db'

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    contact = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50), nullable=False)



@app.route('/vendors')
def vendors():
    vendors = Vendor.query.all()
    return render_template('vendors.html', vendors=vendors)



@app.route('/add_vendor', methods=['GET', 'POST'])
def add_vendor():
    if request.method == 'POST':
        name = request.form.get('name')
        contact = request.form.get('contact')
        email = request.form.get('email')
        phone = request.form.get('phone')
        new_vendor = Vendor(name=name, contact=contact, email=email, phone=phone)
        db.session.add(new_vendor)
        db.session.commit()
        flash('Vendor added successfully!', 'success')
        return redirect(url_for('vendors'))
    return render_template('add_vendor.html')


@app.route('/edit_vendor/<int:id>', methods=['GET', 'POST'])
def edit_vendor(id):
    vendor = Vendor.query.get_or_404(id)
    if request.method == 'POST':
        vendor.name = request.form.get('name')
        vendor.contact = request.form.get('contact')
        vendor.email = request.form.get('email')
        vendor.phone = request.form.get('phone')
        try:
            db.session.commit()
            flash('Vendor updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error updating vendor: {}'.format(str(e)), 'danger')
        return redirect(url_for('vendors'))
    return render_template('edit_vendor.html', vendor=vendor)



@app.route('/delete_vendor/<int:id>')
def delete_vendor(id):
    vendor = Vendor.query.get_or_404(id)
    db.session.delete(vendor)
    db.session.commit()
    flash('Vendor deleted successfully!', 'success')
    return redirect(url_for('vendors'))



















Base = declarative_base()

class WriteUp(Base):
    __tablename__ = 'writeups'
    id = Column(Integer, primary_key=True)
    employee_name = Column(String)
    date = Column(Date)
    reason = Column(String)
    approved = Column(Boolean, default=False)

def fetch_writeups_from_database():
    # Query the WriteUp table to retrieve all write-ups
    writeups = WriteUp.query.all()
    
    # Convert SQLAlchemy objects to dictionaries
    writeups_data = []
    for writeup in writeups:
        writeup_dict = {
            'id': writeup.id,
            'employee_name': writeup.employee_name,
            'date': writeup.date,
            'reason': writeup.reason,
            'approved': writeup.approved
        }
        writeups_data.append(writeup_dict)
    
    return writeups_data

@app.route('/submit_writeup', methods=['POST'])
def submit_writeup():
    employee_name = request.form['employee_name']
    date = request.form['date']
    reason = request.form['reason']
    # Save write-up data to the database
    # Redirect to the write-ups page
    return redirect(url_for('writeups'))

@app.route('/writeups')
def writeups():
    # Fetch writeups from the database (replace with actual database interaction)
    writeups = fetch_writeups_from_database()

    # Render the writeups page with the writeups data
    return render_template('writeups.html', writeups=writeups)

@app.route('/approve_writeup/<int:writeup_id>', methods=['POST'])
def approve_writeup(writeup_id):
    # Find the write-up in the database and update its status to approved
    # Redirect back to the write-ups page
    return redirect(url_for('writeups'))


@app.route('/download_pdf/<int:writeup_id>')
def download_pdf(writeup_id):
    # Fetch write-up data from the database
    # Generate PDF document using ReportLab
    # Return PDF file to the user for download
    response = make_response(pdf_data)
    response.headers['Content-Disposition'] = 'attachment; filename=writeup.pdf'
    response.mimetype = 'application/pdf'
    return response

@app.route('/deny_write_up/<int:write_up_id>', methods=['POST'])
def deny_write_up(write_up_id):
    # Fetch the write-up and delete it
    write_up
    db.session.delete(write_up)
    db.session.commit()
    flash('Write-up has been denied and deleted.', 'success')
    return redirect(url_for('some_route'))  # Redirect to the appropriate page


@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
# Initialize Database
def init_db():
    with sqlite3.connect('application.db') as db:
        # Create the 'users' table if it doesn't exist
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT, 
                password TEXT, 
                first_name TEXT, 
                is_active INTEGER
            )
        ''')
        # Insert an initial admin user if it doesn't exist
        db.execute('''
            INSERT OR IGNORE INTO users (username, password, first_name, is_active) 
            VALUES (?, ?, ?, ?)
        ''', ('admin', '0716', 'Admin', 1))

        # Create the 'write_ups' table if it doesn't exist
        db.execute('''
            CREATE TABLE IF NOT EXISTS write_ups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_name TEXT NOT NULL,
                reason TEXT NOT NULL,
                details TEXT NOT NULL,
                author TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Initialize or modify the 'tips' table
        db.execute('''
            CREATE TABLE IF NOT EXISTS tips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                main_bar_earnings REAL,
                lower_bar_earnings REAL,
                server_earnings REAL,
                num_servers INTEGER,
                num_runners INTEGER
            );
        ''')

        # (Optional) Add columns if you're modifying an existing table
        # You can comment this out after running it once
        # db.execute('ALTER TABLE tips ADD COLUMN main_bar_earnings REAL;')
        # db.execute('ALTER TABLE tips ADD COLUMN lower_bar_earnings REAL;')
        # db.execute('ALTER TABLE tips ADD COLUMN server_earnings REAL;')

        # (Optional) Add 'num_workers' column if you're modifying an existing table
        # You can comment this out after running it once
        # db.execute('ALTER TABLE tips ADD COLUMN num_workers INTEGER;')

        # Initialize or modify the 'beers' table
        db.execute('''
            CREATE TABLE IF NOT EXISTS beers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                beer_number INTEGER NOT NULL,
                price REAL NOT NULL,
                style TEXT NOT NULL,
                name TEXT NOT NULL,
                origin TEXT NOT NULL,
                keg_count INTEGER NOT NULL
            );
        ''')

        db.commit()



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ? AND password = ? AND is_active = 1', (username, password)).fetchone()
        if user:
            session['username'] = user['username']
            # Here, you can also set other session variables as needed
            return redirect(url_for('user_links'))  # Redirect to the user dashboard
        else:
            return render_template('error_page.html', error='Invalid username, password, or account deactivated. Please contact Zach Rabinowitz')

    return render_template('login.html')

pdf_data = {}


@app.route('/sales-report', methods=['GET', 'POST'])
def sales_report():
    if request.method == 'POST':
        # Get the selected date from the form
        selected_date = request.form['selected_date']
        
        # Query Stripe API to get sales data for the selected date
        # You can customize this based on your data structure
        sales_data = fetch_sales_data(selected_date)
        
        # Calculate the total sales amount for the selected date
        total_sales = calculate_total_sales(sales_data)
        
        return render_template('sales_report.html', total_sales=total_sales, sales_data=sales_data)

    return render_template('sales_report.html')

# Define functions to fetch and calculate sales data
def fetch_sales_data(selected_date):
    # Use Stripe API to fetch sales data for the selected date
    # Customize this based on your Stripe data structure
    # Example: stripe.Charge.list(created={'gte': selected_date, 'lt': selected_date + 86400})
    # Return a list of charges or other relevant data
    return []

def calculate_total_sales(sales_data):
    # Calculate the total sales amount from the sales data
    # Example: sum(charge.amount for charge in sales_data)
    return 0



@app.route('/user-links')
def user_links():
    if 'username' not in session:
        return redirect(url_for('login'))

    db = get_db()
    username = session['username']
    user_data = db.execute('SELECT first_name FROM users WHERE username = ?', (username,)).fetchone()

    if user_data is None:
        # Handle case where no user data is found
        return "User not found", 404

    return render_template('user_links.html', first_name=user_data['first_name'])





class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    last_purchased = db.Column(db.Date, nullable=False)
    stock = db.Column(db.Integer, nullable=False)


@app.route('/beer-list', methods=['GET', 'POST'])
def beer_list():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        origin = request.form['origin']
        cost = float(request.form['cost'])
        last_purchased = datetime.strptime(request.form['last_purchased'], '%Y-%m-%d')
        stock = int(request.form['stock'])

        new_beer = Beer(name=name, origin=origin, cost=cost, last_purchased=last_purchased, stock=stock)
        db.session.add(new_beer)
        db.session.commit()
        return redirect(url_for('beer_list'))

    beers = Beer.query.all()
    return render_template('beer_list.html', beers=beers)



@app.route('/edit-beer/<int:beer_id>', methods=['GET', 'POST'])
def edit_beer(beer_id):
    beer = Beer.query.get_or_404(beer_id)

    if request.method == 'POST':
        beer.name = request.form['name']
        beer.origin = request.form['origin']
        beer.cost = float(request.form['cost'])
        beer.last_purchased = datetime.strptime(request.form['last_purchased'], '%Y-%m-%d')
        beer.stock = int(request.form['stock'])

        db.session.commit()
        return redirect(url_for('beer_list'))

    return render_template('edit_beer.html', beer=beer)

@app.route('/delete-beer/<int:beer_id>', methods=['POST'])
def delete_beer(beer_id):
    beer = Beer.query.get_or_404(beer_id)
    db.session.delete(beer)
    db.session.commit()
    return redirect(url_for('beer_list'))



# Replace this function with your database query to get write-up details
def get_write_up_details(write_up_id):
   # Your database query logic here
   # You should return the write-up details as a dictionary
   return {
       'Employee Name': 'John Doe',
       'Reason': 'Performance Issue',
       'Details': 'Employee had multiple late arrivals.',
       'Author': 'Manager A',
       'Date': '2023-01-15',
   }

inventory_data = [
    {"name": "Item 1", "category": "Food", "quantity": 10},
    {"name": "Item 2", "category": "Food", "quantity": 15},
    {"name": "Item 3", "category": "Liquor", "quantity": 20},
    # Add more items and categories as needed
]






@app.route('/inventory', methods=['GET', 'POST'])
def manage_inventory():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        origin = request.form['origin']
        cost = float(request.form['cost'])
        last_purchased = datetime.strptime(request.form['last_purchased'], '%Y-%m-%d')
        stock = int(request.form['stock'])

        new_item = InventoryItem(name=name, origin=origin, cost=cost, last_purchased=last_purchased, stock=stock)
        db.session.add(new_item)
        db.session.commit()
        flash('Item added successfully!', 'success')
        return redirect(url_for('manage_inventory'))

    items = InventoryItem.query.all()
    return render_template('manage_inventory.html', items=items)

@app.route('/inventory/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_inventory(item_id):
    item = InventoryItem.query.get_or_404(item_id)

    if request.method == 'POST':
        item.name = request.form['name']
        item.origin = request.form['origin']
        item.cost = float(request.form['cost'])
        item.last_purchased = datetime.strptime(request.form['last_purchased'], '%Y-%m-%d')
        item.stock = int(request.form['stock'])

        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect(url_for('manage_inventory'))

    return render_template('edit_inventory.html', item=item)

@app.route('/inventory/delete/<int:item_id>', methods=['POST'])
def delete_inventory(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!', 'success')
    return redirect(url_for('manage_inventory'))

class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    last_purchased = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<InventoryItem {self.name}>'


@app.route('/export_inventory')
def export_inventory():
    items = Item.query.all()
    item_list = [{"ID": i.id, 
                  "Name": i.name, 
                  "Quantity": i.quantity, 
                  "Price": i.price, 
                  "Description": i.description} for i in items]
    df = pd.DataFrame(item_list)
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    return send_file(output, mimetype='text/csv', download_name='inventory.csv', as_attachment=True)

@app.route('/import_inventory', methods=['GET', 'POST'])
def import_inventory():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            flash('No file selected', 'danger')
            return redirect(request.url)
        try:
            df = pd.read_csv(file)
            added_count = 0
            for index, row in df.iterrows():
                if 'Name' in row and 'Quantity' in row and 'Price' in row:
                    new_item = Item(
                        name=row['Name'],
                        quantity=int(row['Quantity']),
                        price=float(row['Price']),
                        description=row.get('Description', '')
                    )
                    db.session.add(new_item)
                    added_count += 1
                else:
                    flash('CSV file is missing required columns', 'danger')
                    return redirect(request.url)
            db.session.commit()
            flash(f'{added_count} items imported successfully!', 'success')
        except KeyError as e:
            flash(f'CSV file is missing the required column: {e}', 'danger')
        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
        return redirect(url_for('inventory'))
    return render_template('import_inventory.html')

















class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)




with app.app_context():
    db.create_all() 


def add_demo_items():
    # Add demo items to the database
    if Item.query.count() == 0:  # Add items only if the table is empty
        demo_items = [
            Item(name='Apple', quantity=100, price=0.50, description='Fresh Red Apples'),
            Item(name='Banana', quantity=150, price=0.30, description='Organic Bananas'),
            Item(name='Orange', quantity=120, price=0.80, description='Juicy Oranges'),
            Item(name='Milk', quantity=50, price=1.20, description='Whole Milk'),
            Item(name='Bread', quantity=60, price=1.50, description='Wheat Bread'),
        ]
        db.session.bulk_save_objects(demo_items)
        db.session.commit()


@app.route('/inventory', methods=['GET'])
def show_inventory_page():
    try:
        search_query = request.args.get('search', '')
        if search_query:
            items = Item.query.filter(
                db.or_(
                    Item.name.ilike(f'%{search_query}%'),
                    Item.description.ilike(f'%{search_query}%')
                )
            ).all()
        else:
            items = Item.query.all()
        return render_template('inventory.html', items=items)
    except Exception as e:
        return f"An error occurred while fetching inventory items: {e}"

@app.route('/add-item', methods=['POST'])
def add_item():
    try:
        name = request.form.get('name')
        quantity = request.form.get('quantity', type=int)
        price = request.form.get('price', type=float)
        description = request.form.get('description')

        if not name or not quantity or not price:
            flash('Name, Quantity, and Price are required!', 'danger')
            return redirect(url_for('show_inventory_page'))

        new_item = Item(name=name, quantity=quantity, price=price, description=description)
        db.session.add(new_item)
        db.session.commit()
        flash('Item added successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred while adding the item: {e}', 'danger')
    return redirect(url_for('show_inventory_page'))
# Define a placeholder inventory data structure (replace with your actual data storage)
inventory = [

    # Add more items as needed
]






# Define the Item model


@app.route
def create_tables():
    db.create_all()
    


@app.route('/edit-item/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.query.get_or_404(item_id)
    if request.method == 'POST':
        try:
            item.name = request.form.get('name')
            item.quantity = request.form.get('quantity', type=int)
            item.price = request.form.get('price', type=float)
            item.description = request.form.get('description')

            db.session.commit()
            flash('Item updated successfully!', 'success')
            return redirect(url_for('show_inventory_page'))
        except Exception as e:
            flash(f'An error occurred while updating the item: {e}', 'danger')
            return redirect(url_for('edit_item', item_id=item_id))
    return render_template('edit_item.html', item=item)


@app.route('/delete-item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    try:
        db.session.delete(item)
        db.session.commit()
        flash('Item deleted successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred while deleting the item: {e}', 'danger')
    return redirect(url_for('show_inventory_page'))



@app.route('/items')
def list_items():
    items = Item.query.all()
    return render_template('list_items.html', items=items)


@app.route('/tips', methods=['GET', 'POST'])
def manage_tips():
    db = get_db()
    tip_info = None

    if request.method == 'POST':
        # Collect the earnings and number of workers
        main_bar_earnings = float(request.form['main_bar_earnings'])
        lower_bar_earnings = float(request.form['lower_bar_earnings'])
        server_earnings = float(request.form['server_earnings'])
        num_servers = int(request.form['num_servers'])
        num_runners = int(request.form['num_runners'])

        # Calculate the total earnings and tips for runners
        total_earnings = main_bar_earnings + lower_bar_earnings + server_earnings
        tips_for_runners = (total_earnings * 0.08) / num_runners if num_runners > 0 else 0

        # Store the information in the database
        date = request.form['date']
        db.execute('INSERT INTO tips (date, main_bar_earnings, lower_bar_earnings, server_earnings, num_servers, num_runners) VALUES (?, ?, ?, ?, ?, ?)',
                   (date, main_bar_earnings, lower_bar_earnings, server_earnings, num_servers, num_runners))
        db.commit()

        tip_info = {
            'total_earnings': total_earnings,
            'tips_per_runner': tips_for_runners
        }

    return render_template('manage_tips.html', tip_info=tip_info)

# Sample write-up dictionary (replace with your actual data retrieval logic)
write_ups = {
    1: {
        'id': 1,
        'employee_name': 'John Doe',
        'reason': 'Performance Issue',
        'details': 'Employee had multiple late arrivals.',
        'author': 'Manager A',
        'created_at': '2023-01-15',
    },
    2: {
        'id': 2,
        'employee_name': 'Jane Smith',
        'reason': 'Customer Complaint',
        'details': 'Rude behavior reported by customers.',
        'author': 'Manager B',
        'created_at': '2023-01-16',
    },
    # Add more write-ups as needed
}




purchase_requests_list = []



# ...
# New routes for purchase requests
@app.route('/purchasing_requests', methods=['GET', 'POST'])
def purchasing_requests():
    if request.method == 'POST':
        item_name = request.form.get('item_name')
        price = request.form.get('price')
        reason = request.form.get('reason')
        other_details = request.form.get('other_details')
        requester = request.form.get('requester')
        approver = request.form.get('approver')

        # Create a new purchase request dictionary
        new_request = {
            'item_name': item_name,
            'price': price,
            'reason': reason,
            'other_details': other_details,
            'requester': requester,
            'approver': approver,
            'status': 'Pending'  # Initial status is set to Pending
        }

        # Append the new request to the list of purchase_requests
        purchase_requests_list.append(new_request)

    return render_template('purchasing_requests.html', purchase_requests=purchase_requests_list)



@app.route('/submit_request', methods=['POST'])
def submit_request():
    item_name = request.form.get('item_name')
    need_for_item = request.form.get('need_for_item')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    requesting_manager = request.form.get('requesting_manager')
    approving_manager = request.form.get('approving_manager')

    # Create a new purchase request dictionary
    new_request = {
        'item_name': item_name,
        'need_for_item': need_for_item,
        'price': price,
        'quantity': quantity,
        'requesting_manager': requesting_manager,
        'approving_manager': approving_manager,
        'status': 'Pending'  # Initial status is set to Pending
    }

    # Append the new request to the list of purchase_requests
    purchase_requests_list.append(new_request)

    return redirect('/')

# Implement approve and deny functionality
@app.route('/approve_request/<int:index>', methods=['POST'])
def approve_request(index):
    if 0 <= index < len(purchase_requests_list):
        request_to_approve = purchase_requests_list[index]
        request_to_approve['status'] = 'Approved'
        
        # Generate a PDF for approved request
        pdf_buffer = generate_purchase_request_pdf(request_to_approve)
        
        # Create a Flask response with the PDF content
        response = Response(pdf_buffer, content_type='application/pdf')
        response.headers['Content-Disposition'] = f'attachment; filename=purchase_request_{index}.pdf'
        
        return response
    return redirect('/purchasing_requests')



@app.route('/deny_request/<int:index>', methods=['POST'])
def deny_request(index):
    if 0 <= index < len(purchase_requests_list):
        request_to_deny = purchase_requests_list.pop(index)  # Remove the request from the list
        return redirect('/purchasing_requests')
    return redirect('/purchasing_requests')

def generate_purchase_request_pdf(request_data):
    pdf_buffer = io.BytesIO()
    p = canvas.Canvas(pdf_buffer)

    # Use request_data to populate the PDF content
    p.drawString(100, 790, F'The Draft Room: Human Resources Department')
    p.drawString(100, 770, F'Employee Write Up Form')
    p.drawString(100, 750, f'Employee Name: {request_data["item_name"]}')
    p.drawString(100, 730, f'Employee #: {request_data["price"]}')
    p.drawString(100, 710, f'Reason: {request_data["reason"]}')
    p.drawString(100, 690, f'Other Details: {request_data["other_details"]}')
    p.drawString(100, 670, f'Requester: {request_data["requester"]}')
    p.drawString(100, 650, f'Approver: {request_data["approver"]}')
    p.drawString(50, 630, F'This document will be kept with the Human Resources Department in the employees records.')

    p.save()
    pdf_buffer.seek(0)
    return pdf_buffer






@app.route('/manage-users', methods=['GET', 'POST'])
def manage_users():
    if 'username' not in session:
        return redirect(url_for('login'))

    db = get_db()  # Ensure db is defined by calling get_db()

    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']  # Hash this password in production
            first_name = request.form['first_name']
            db.execute('INSERT INTO users (username, password, first_name, is_active) VALUES (?, ?, ?, ?)',
                       (username, password, first_name, 1))
            db.commit()
        except sqlite3.Error as e:
            print("Database error:", e)
            # Handle the database error appropriately

    try:
        users = db.execute('SELECT * FROM users').fetchall()
    except sqlite3.Error as e:
        print("Database error:", e)
        users = []  # Default to an empty list in case of a database read error

    return render_template('manage_users.html', users=users)



@app.route('/write_up/<int:write_up_id>')
def view_write_up(write_up_id):
    # Retrieve the write-up details from the 'write_ups' dictionary (replace with your DB query)
    write_up = write_ups.get(write_up_id)

    if not write_up:
        # Handle the case where the write-up with the given ID doesn't exist
        return 'Write-up not found', 404

    # Render the 'write_up.html' template and pass the 'write_up' variable to it
    return render_template('write_up.html', write_up=write_up)

@app.route('/write-up', methods=['GET', 'POST'])
def write_up():
    if 'username' not in session:
        return redirect(url_for('login'))

    db = get_db()

    if request.method == 'POST':
        if 'employee_name' in request.form:
            # Handle new write-up submission
            employee_name = request.form['employee_name']
            reason = request.form['reason']
            details = request.form['details']

            db.execute('INSERT INTO write_ups (employee_name, reason, details, author) VALUES (?, ?, ?, ?)',
                       (employee_name, reason, details, session['username']))
            db.commit()
        else:
            # Handle "Approve" or "Deny" actions
            write_up_id = request.form.get('action_id')
            if 'approve' in request.form:
                db.execute('UPDATE write_ups SET is_approved = 1 WHERE id = ?', (write_up_id,))
            elif 'deny' in request.form:
                db.execute('DELETE FROM write_ups WHERE id = ?', (write_up_id,))
            db.commit()

    write_ups = db.execute('SELECT * FROM write_ups WHERE is_approved IS NULL OR is_approved = 1').fetchall()
    return render_template('write_up_form.html', write_ups=write_ups)
    



@app.route('/toggle-user/<username>')
def toggle_user(username):
    if 'username' not in session:
        return redirect(url_for('login'))

    db = get_db()
    user = db.execute('SELECT is_active FROM users WHERE username = ?', (username,)).fetchone()

    if user:
        new_status = 0 if user['is_active'] else 1
        db.execute('UPDATE users SET is_active = ? WHERE username = ?', (new_status, username))
        db.commit()
    else:
        # Handle case if user is not found
        print("User not found")

    return redirect(url_for('manage_users'))

@app.route('/update-db')
def update_db():
    db = get_db()
    db.execute('ALTER TABLE write_ups ADD COLUMN is_approved INTEGER')
    db.commit()
    return "Database updated."


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

with app.app_context():
    db.create_all()

    
if __name__ == '__main__':
    init_db()  # Initialize the database, can be commented out after the first run
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
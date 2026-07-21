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
from sqlalchemy.ext.declarative import declarative_base
from reportlab.pdfgen import canvas
from flask import request, redirect
from flask import render_template, request, redirect, url_for, jsonify
from flask_login import current_user
from app import db
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key =  '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'
 # Replace with your actual secret key



login_manager = LoginManager()
login_manager.login_view = 'login'  # Specify the view for login
login_manager.init_app(app)


# Configure your SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
stripe.api_key = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Adjust this URI to your actual database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to your secret key

app = Flask(__name__)
app.secret_key = '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'  # Replace with your actual secret key


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Member {self.first_name} {self.last_name}>'
with app.app_context():
    db.create_all() 






# Route for adding a new member
@app.route('/add-member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        
        new_member = Member(first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_member)
        db.session.commit()
        
        return redirect(url_for('show_members_page'))
    return render_template('add_member.html')

# Dummy data for member profiles
member_profiles = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john@example.com", "phone": "123-456-7890", "membership_level": "Gold"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "email": "jane@example.com", "phone": "987-654-3210", "membership_level": "Silver"},
    # Add more member profiles here if needed
]

# Route for member profile page
@app.route('/member/<int:member_id>')
def member_profile(member_id):
    member = Member.query.get_or_404(member_id)
    orders = Order.query.filter_by(member_id=member_id).all()
    notes = Note.query.filter_by(member_id=member_id).all()
    return render_template('member_profile.html', member=member, orders=orders, notes=notes)

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
@app.route('/edit_member/<int:member_id>', methods=['GET', 'POST'])
def edit_member(member_id):
    member = Member.query.get_or_404(member_id)
    if request.method == 'POST':
        member.first_name = request.form['first_name']
        member.last_name = request.form['last_name']
        member.email = request.form['email']
        db.session.commit()
        return redirect(url_for('show_members_page'))
    return render_template('edit_member.html', member=member)


# Route to delete a member
@app.route('/delete_member/<int:member_id>', methods=['POST'])
def delete_member(member_id):
    member = Member.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('show_members_page'))



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
@app.route('/members')
def members():
    return render_template('members.html', members=members_data)

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
    return render_template('order_history.html', member=member, orders=orders)

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

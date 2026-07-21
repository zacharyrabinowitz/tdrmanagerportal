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
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, g
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request, redirect, url_for
import PyPDF2


app = Flask(__name__)
app.secret_key =  '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'
 # Replace with your actual secret key

# Configure your SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with your actual secret key

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

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.route('/', endpoint='home')
def index():
    return render_template('order.html', catalog=catalog, cart=cart)


# Sample catalog data (you can replace this with your actual data)
catalog = [
    {"id": 1, "name": "Item 1", "price": 10.0},
    {"id": 2, "name": "Item 2", "price": 15.0},
    {"id": 3, "name": "Item 3", "price": 12.0},
]

cart = []


# Dummy list to store member information (you can replace this with a database)
members = []


@app.route('/members', methods=['GET', 'POST'])
def show_members_page():
    if request.method == 'POST':
        # Get member information from the form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']

        # Create a dictionary to represent a member
        member = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number
        }

        # Add the member to the list
        members.append(member)

    return render_template('members.html', members=members)
# Route for adding a new member
@app.route('/add-member', methods=['POST'])
def add_member():
    global member_profiles
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']

        # Generate a unique ID for the new member
        new_member_id = len(member_profiles) + 1

        # Create a new member profile
        new_member = {
            "id": new_member_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "membership_level": "Standard"  # Default membership level
        }

        # Add the new member profile to the list
        member_profiles.append(new_member)

        return redirect(url_for('member_profile', id=new_member_id))

# Dummy data for member profiles
member_profiles = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john@example.com", "phone": "123-456-7890", "membership_level": "Gold"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "email": "jane@example.com", "phone": "987-654-3210", "membership_level": "Silver"},
    # Add more member profiles here if needed
]

# Route for member profile page
@app.route('/member-profile', methods=['GET'])
def member_profile():
    # Get the member ID from the URL query parameters
    member_id = request.args.get('id')

    # Find the member profile with the given ID
    member_profile = None
    for profile in member_profiles:
        if str(profile["id"]) == member_id:
            member_profile = profile
            break

    if member_profile:
        return render_template('member_profile.html', member=member_profile)
    else:
        return "Member not found", 404
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
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']

        for member in members_data:
            if member['id'] == member_id:
                member['first_name'] = first_name
                member['last_name'] = last_name
                member['email'] = email
                member['phone'] = phone

                return redirect(url_for('members'))

    for member in members_data:
        if member['id'] == member_id:
            return render_template('edit_member.html', member=member)

    return redirect(url_for('members'))

# Route to delete a member
@app.route('/delete_member/<int:member_id>', methods=['GET', 'POST'])
def delete_member(member_id):
    if request.method == 'POST':
        for member in members_data:
            if member['id'] == member_id:
                members_data.remove(member)
                return redirect(url_for('members'))

    for member in members_data:
        if member['id'] == member_id:
            return render_template('delete_member.html', member=member)

    return redirect(url_for('members'))

# Route to display members list
@app.route('/members')
def members():
    return render_template('members.html', members=members_data)


@app.route('/')
def index():
    return render_template('index.html', pdf_data=pdf_data)

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

@app.route('/place_order', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        item_id = int(request.form.get('item_id'))
        quantity = int(request.form.get('quantity'))

        # Find the selected item in the catalog
        selected_item = next((item for item in catalog if item["id"] == item_id), None)

        if selected_item and quantity > 0:
            item_to_add = {
                "item_id": selected_item["id"],
                "name": selected_item["name"],
                "price": selected_item["price"],
                "quantity": quantity,
            }
            cart.append(item_to_add)

    return render_template('place_order.html', catalog=catalog, cart=cart)

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


# Define role constants
ROLE_MANAGER = 'Manager'
ROLE_ADMIN = 'Admin'
ROLE_EMPLOYEE = 'Employee'


# Function to generate a PDF for an approved write-up
def generate_pdf(write_up_details):
    # Create a PDF document
    pdf_buffer = io.BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    
    # Define custom styles
    styles = getSampleStyleSheet()
    custom_style = styles["Normal"]
    custom_style.fontName = "Helvetica-Bold"
    custom_style.fontSize = 12
    custom_style.textColor = colorama.black
    
    # Create a list of elements to add to the PDF
    elements = []

    # Use the custom style for each paragraph
    elements.append(Paragraph(f'<b>Employee Name:</b> {write_up_details["Employee Name"]}', custom_style))
    elements.append(Paragraph(f'<b>Reason:</b> {write_up_details["Reason"]}', custom_style))
    elements.append(Paragraph(f'<b>Details:</b> {write_up_details["Details"]}', custom_style))
    elements.append(Paragraph(f'<b>Author:</b> {write_up_details["Author"]}', custom_style))
    elements.append(Paragraph(f'<b>Date:</b> {write_up_details["Date"]}', custom_style))

    # Build the PDF document
    doc.build(elements)

    pdf_buffer.seek(0)
    return pdf_buffer
# Function to generate a PDF for an approved write-up
def generate_write_up_pdf(write_up_details):
    pdf_buffer = io.BytesIO()
    p = canvas.Canvas(pdf_buffer)

    # Use the write-up details to populate the PDF content
    p.drawString(100, 750, f'Employee Name: {write_up_details["Employee Name"]}')
    p.drawString(100, 730, f'Reason: {write_up_details["Reason"]}')
    p.drawString(100, 710, f'Details: {write_up_details["Details"]}')
    p.drawString(100, 690, f'Author: {write_up_details["Author"]}')
    p.drawString(100, 670, f'Date: {write_up_details["Date"]}')

    p.save()
    pdf_buffer.seek(0)
    return pdf_buffer

# Modify the 'approve_write_up' route to include the delete logic
@app.route('/approve_write_up/<int:write_up_id>')
# Add this function to your code
def delete_write_up(write_up_id):
    db = get_db()  # Get the database connection
    try:
        # Implement your logic to delete the write-up with the given ID
        # Here, we assume you have a 'write_ups' table with an 'id' column.
        db.execute('DELETE FROM write_ups WHERE id = ?', (write_up_id,))
        db.commit()
    except sqlite3.Error as e:
        print("Database error:", e)
        # Handle the database error appropriately, e.g., log it or display an error message

def approve_write_up(write_up_id):

    # Retrieve write-up details from the database
    write_up_details = get_write_up_details(write_up_id)  # Replace with your database query

    # Generate the PDF
    pdf_buffer = generate_pdf(write_up_details)

    # Create a Flask response with the PDF content
    response = Response(pdf_buffer, content_type='application/pdf')
    response.headers['Content-Disposition'] = f'inline; filename=write_up_{write_up_id}.pdf'

    # Delete the write-up after serving the PDF for download
    delete_write_up(write_up_id)
    return response
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
        ''', ('admin', '0176', 'Admin', 1))

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
            return render_template('login.html', error='Invalid username, password, or account deactivated')

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
@app.route('/beer-list', methods=['GET', 'POST'])
def beer_list():
    db = get_db()

    if request.method == 'POST':
        if 'new_beer' in request.form:
            # Add a new beer
            new_beer_details = {
                'beer_number': request.form['new_beer_number'],
                'price': request.form['new_price'],
                'style': request.form['new_style'],
                'name': request.form['new_name'],
                'origin': request.form['new_origin'],
                'keg_count': request.form['new_keg_count']
            }
            db.execute('''
                INSERT INTO beers (beer_number, price, style, name, origin, keg_count) 
                VALUES (:beer_number, :price, :style, :name, :origin, :keg_count)
            ''', new_beer_details)
        else:
            # Update existing beer
            beer_id = request.form['beer_id']
            beer_number = request.form['beer_number']
            name = request.form['name']
            style = request.form['style']
            origin = request.form['origin']
            price = request.form['price']
            keg_count = request.form['keg_count']

            db.execute('''
                UPDATE beers SET 
                beer_number = ?, 
                name = ?, 
                style = ?, 
                origin = ?, 
                price = ?, 
                keg_count = ? 
                WHERE id = ?
            ''', (beer_number, name, style, origin, price, keg_count, beer_id))

            db.commit()
        return redirect(url_for('beer_list'))

    beers = db.execute('SELECT * FROM beers').fetchall()
    return render_template('beer_list.html', beers=beers)

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

@app.route('/inventory')
def inventory():
    return render_template('inventory.html', inventory=inventory_data)

@app.route('/add_item', methods=['POST'])
def add_item():
    if request.method == 'POST':
        new_item = {
            "id": len(inventory_data) + 1,
            "name": request.form['name'],
            "category": request.form['category'],
            "quantity": int(request.form['quantity'])
        }
        inventory_data.append(new_item)
    return redirect(url_for('inventory'))

@app.route('/edit_item', methods=['POST'])
def edit_item():
    if request.method == 'POST':
        item_id = request.form['edit_item_id']
        new_name = request.form['edit_name']
        new_category = request.form['edit_category']
        new_quantity = request.form['edit_quantity']

        # Assuming you have an Item model, update the item in the database
        item = itemgetter.query.get(item_id)
        item.name = new_name
        item.category = new_category
        item.quantity = new_quantity
        db.session.commit()

        # Redirect back to the inventory page after editing
        return redirect(url_for('inventory'))

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
    p.drawString(100, 750, f'Item Name: {request_data["item_name"]}')
    p.drawString(100, 730, f'Price: {request_data["price"]}')
    p.drawString(100, 710, f'Reason: {request_data["reason"]}')
    p.drawString(100, 690, f'Other Details: {request_data["other_details"]}')
    p.drawString(100, 670, f'Requester: {request_data["requester"]}')
    p.drawString(100, 650, f'Approver: {request_data["approver"]}')

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

if __name__ == '__main__':
    init_db()  # Initialize the database, can be commented out after the first run
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)
    

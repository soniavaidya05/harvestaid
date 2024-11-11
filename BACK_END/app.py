from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from user_dash import signup_func, login_func, get_user_by_username
from secretkey import sk
from User import User
import json
from werkzeug.utils import secure_filename
import os
from search_engine import searchFor

app = Flask(__name__)
app.secret_key = sk

UPLOAD_FOLDER = 'BACK_END/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

try:
    with open('client_logins.json', 'r') as file:
        client_logins = json.load(file)
except json.JSONDecodeError:
    client_logins = {}  
    

def load_products():
    try:
        with open('listingdatabase.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if the file is missing or empty


@app.route('/')  
def get_started():
    return render_template('landingPage.html')

@app.route('/listings_dir')  
def index():
    if 'username' not in session:
        return redirect(url_for('login_view'))  # Require login to access listings
    return render_template('listings_template.html')

@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login_func(username, password):
            session['username'] = username  # Store user session 
            return redirect(url_for('index'))  # Redirect to listings page on successful login
        else:
            return redirect(url_for('login_view'))  # Redirect back to login page if login fails
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup_view():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        signed_in = signup_func(username, email, password)
        if signed_in:
            return redirect(url_for('login_view'))  # Redirect to login page on successful signup
        else:
            return redirect(url_for('signup_view'))  # Redirect back to signup page if signup fails
    return render_template('signup.html')

@app.route('/listings', methods=['GET'])
def get_products():
    products = load_products()
    category = request.args.get('category')  # Get the category from query parameters
    if category:
        # Filter products by category
        products = [product for product in products if product.get('category') == category]
    return jsonify(products)

@app.route('/searchProducts', methods=['GET'])
def search_products():
    #Loading Products.
    products = load_products()
    phrase = request.args.get('phrase')
    products = searchFor(phrase, products)
    return jsonify(products)

def save_products(products):
    """Save the updated products list to listingdatabase.json."""
    with open('listingdatabase.json', 'w') as f:
        json.dump(products, f, indent=4)


@app.route('/productPage')
def product_page():
    return render_template('productPage.html')


@app.route('/addListing', methods=['GET', 'POST'])
def new_listing():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        location = request.form['location']
    
        # Process image if uploaded
        picture = request.files.get('picture')
        picture_path = None
        image_url = None
        if picture:
            filename = secure_filename(picture.filename)
            picture_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save the image in the upload folder
            picture.save(picture_path)

            # Use the relative path for the URL, stored in the database as 'uploads/filename'
            image_url = f'/static/images/{filename}'

        
        username = session['username']  # Get the current logged-in user
        user = get_user_by_username(username)  # Access the user object from the clients dictionary
        user.new_listing(category, title, location, description, image_url)
        products = load_products()  # Reload products after adding a new one
        save_products(products)
        # if user:
        #     # Call the new_listing method from User
        #     user.new_listing(category, title, location, description, picture_path)

        #     # Optionally save all products if needed
        #     products = load_products()  # Reload products after adding a new one
        #     save_products(products)

        return redirect(url_for('index'))  # Redirect to listings page
    
    # If GET request, render the form page
    return render_template('addListing.html')


if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production

# @app.route('/listings/<int:listing_id>', methods=['GET'])
# def product_details(listing_id):
#     products = load_products()
#     listing = next((p for p in products if int(p.get('product name', -1)) == listing_id), None)
#     if listing:
#         return render_template('productPage.html', listing=listing)
#     else:
#         return "Product not found", 404

# from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, session
# from user_dash import signup, login
# import json

# app = Flask(__name__)

# def load_products():
#     with open('listingdatabase.json') as f:
#         return json.load(f)

# @app.route('/')  # Landing page route
# def get_started():
#     return render_template('landingPage.html')

# @app.route('/listingtemp')  # Listings page route
# def index():
#     return render_template('listings_template.html')

# # @app.route('/')
# # def get_started():
# #     return render_template('landingPage.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login_view():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if login(username, password):
#             session['username'] = username  # Store user session for authenticated state
#             return redirect(url_for('index'))  # Redirect to listings page on successful login
#         else:
#             return redirect(url_for('login_view'))  # Redirect back to login page if login fails
#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup_view():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if signup(username, password):
#             return redirect(url_for('login_view'))  # Redirect to login page on successful signup
#         else:
#             return redirect(url_for('signup_view'))  # Redirect back to signup page if signup fails
#     return render_template('signup.html')

# @app.route('/loginPage')
# def login_page():
#     return render_template('login.html')

# @app.route('/signupPage')
# def signup_page():
#     return render_template('signup.html')

# # @app.route('/')
# # def index():
# #     return render_template('listings_template.html')

# @app.route('/listings', methods=['GET'])
# def get_products():
#     products = load_products()
#     category = request.args.get('category')  # Get the category from query parameters
#     if category:
#         # Filter products by category
#         products = [product for product in products if product['category'] == category]
#     return jsonify(products)

# # @app.route('/listings', methods=['GET'])
# # def get_products():
# #     # if 'username' not in session:
# #     #     return redirect(url_for('login_view'))  # Redirect to login if not logged in

# #     products = load_products()
# #     category = request.args.get('category')  # Get the category from query parameters
# #     if category:
# #         # Filter products by category
# #         products = [product for product in products if product['category'] == category]
# #         for product in products:
# #             product['link'] = url_for('product_details', listing_id=product['product name'], _external=True)
# #     return jsonify(products)

# # @app.route('/listings/<int:listing_id>', methods=['GET'])
# # def product_details(listing_id):
# #     products = load_products()
# #     listing = next((p for p in products if p['product name'] == listing_id), None)
# #     if listing:
# #         return render_template('productPage.html', listing=listing)
# #     else:
# #         return "Product not found", 404

# # @app.route('/listings/<int:listing_id>', methods=['GET'])
# # def product_details(listing_id):
# #     # if 'username' not in session:
# #     #     return redirect(url_for('login_view'))  # Redirect to login if not logged in

# #     products = load_products()
# #     listing = next((p for p in products if p['product name'] == listing_id), None)
# #     if listing:
# #         return render_template('productPage.html', listing=listing)
# #     else:
# #         return "Product not found", 404

# @app.route('/productPage')
# def product_page():
#     return render_template('productPage.html')
    
# # @app.route('/index')
# # def index():
# #     if 'username' not in session:
# #         return redirect(url_for('login_view'))  # Redirect to login if not logged in
# #     return render_template('listings_template.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, session
from user_dash import signup, login
import json

app = Flask(__name__)

def load_products():
    with open('listingdatabase.json') as f:
        return json.load(f)

# @app.route('/')
# def get_started():
#     return render_template('landingPage.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login_view():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if login(username, password):
#             session['username'] = username  # Store user session for authenticated state
#             return redirect(url_for('index'))  # Redirect to listings page on successful login
#         else:
#             flash("Invalid username or password. Please try again.")  # Show error message
#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup_view():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if signup(username, password):
#             return redirect(url_for('login_view'))  # Redirect to login page on successful signup
#         else:
#             flash("Signup failed. Username already exists. Please try again.")  # Show error message
#     return render_template('signup.html')

@app.route('/')
def index():
    return render_template('listings_template.html')

@app.route('/listings', methods=['GET'])
def get_products():
    products = load_products()
    category = request.args.get('category')  # Get the category from query parameters
    if category:
        # Filter products by category
        products = [product for product in products if product['category'] == category]
    return jsonify(products)

# @app.route('/listings', methods=['GET'])
# def get_products():
#     # if 'username' not in session:
#     #     return redirect(url_for('login_view'))  # Redirect to login if not logged in

#     products = load_products()
#     category = request.args.get('category')  # Get the category from query parameters
#     if category:
#         # Filter products by category
#         products = [product for product in products if product['category'] == category]
#         for product in products:
#             product['link'] = url_for('product_details', listing_id=product['product name'], _external=True)
#     return jsonify(products)

# @app.route('/listings/<int:listing_id>', methods=['GET'])
# def product_details(listing_id):
#     products = load_products()
#     listing = next((p for p in products if p['product name'] == listing_id), None)
#     if listing:
#         return render_template('productPage.html', listing=listing)
#     else:
#         return "Product not found", 404

@app.route('/listings/<int:listing_id>', methods=['GET'])
def product_details(listing_id):
    # if 'username' not in session:
    #     return redirect(url_for('login_view'))  # Redirect to login if not logged in

    products = load_products()
    listing = next((p for p in products if p['product name'] == listing_id), None)
    if listing:
        return render_template('productPage.html', listing=listing)
    else:
        return "Product not found", 404
    
# @app.route('/index')
# def index():
#     if 'username' not in session:
#         return redirect(url_for('login_view'))  # Redirect to login if not logged in
#     return render_template('listings_template.html')

if __name__ == '__main__':
    app.run(debug=True)
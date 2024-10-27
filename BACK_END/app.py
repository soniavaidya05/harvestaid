from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

def load_products():
    with open('listingdatabase.json') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('listings_template.html')

@app.route('/listings', methods=['GET'])
def get_products():
    products = load_products()
    category = request.args.get('category')  # Get the category from query parameters
    return jsonify(products)

@app.route('/listings/<int:listing_id>', methods=['GET'])
def product_details(listing_id):
    products = load_products()
    listing = next((p for p in products if p['product name'] == listing_id), None)
    if listing:
        return render_template('productPage.html', listing=listing)
    else:
        return "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)
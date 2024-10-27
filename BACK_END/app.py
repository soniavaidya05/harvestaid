from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_products():
    with open('listingdatabase.json') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('listings_template.html')

@app.route('/products', methods=['GET'])
def get_products():
    products = load_products()
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
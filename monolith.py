# monolith.py

from flask import Flask, jsonify

# Create the main application object
app = Flask(__name__)

# This is our in-memory "database". In a real monolith, this would
# likely be a connection to a single SQL database.
PRODUCTS = [
    {'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 1200},
    {'id': 2, 'name': 'Standing Desk', 'category': 'Furniture', 'price': 450},
    {'id': 3, 'name': 'Mechanical Keyboard', 'category': 'Electronics', 'price': 150},
    {'id': 4, 'name': 'Monitor', 'category': 'Electronics', 'price': 300}
]

# --- API Endpoints ---
# All our application's "features" (endpoints) are defined here together.

@app.route('/products', methods=['GET'])
def get_products():
    """
    This is the "List Products" feature.
    It returns the entire list of products.
    """
    return jsonify(PRODUCTS)


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    """
    This is the "Product Details" feature.
    It finds a single product by its ID and returns it.
    """
    # In a real app, you would query the database for this ID.
    # Here, we just search through our list.
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)

    if product:
        return jsonify(product)
    else:
        # Standard practice is to return a 404 Not Found error.
        return jsonify({'error': 'Product not found'}), 404

# This is the standard Python entry point.
# When you run "python3 monolith.py", this code will execute.
if __name__ == '__main__':
    print("Monolith service running on http://127.0.0.1:5000")
    # We run the app on port 5000.
    app.run(port=5000, debug=True)
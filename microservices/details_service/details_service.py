from flask import Flask, jsonify

app = Flask(__name__)

# This service also has its own data. This duplication is for simplicity
# in our exercise. We'll discuss data strategies later.
PRODUCTS = [
    {'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 1200},
    {'id': 2, 'name': 'Standing Desk', 'category': 'Furniture', 'price': 450},
    {'id': 3, 'name': 'Mechanical Keyboard', 'category': 'Electronics', 'price': 150},
    {'id': 4, 'name': 'Monitor', 'category': 'Electronics', 'price': 300}
]

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    """
    This service has ONLY ONE feature: getting details for a specific product.
    """
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    # IMPORTANT: We run this on another unique port, 5002.
    print("Details Service running on http://127.0.0.1:5002")
    app.run(host='0.0.0.0', port=5002, debug=True)
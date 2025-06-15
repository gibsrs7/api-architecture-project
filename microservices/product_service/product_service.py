from flask import Flask, jsonify

app = Flask(__name__)

# This service has its own copy of the data.
# In a real system, this would be its own database connection.
PRODUCTS = [
    {'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 1200},
    {'id': 2, 'name': 'Standing Desk', 'category': 'Furniture', 'price': 450},
    {'id': 3, 'name': 'Mechanical Keyboard', 'category': 'Electronics', 'price': 150},
    {'id': 4, 'name': 'Monitor', 'category': 'Electronics', 'price': 300}
]

@app.route('/products', methods=['GET'])
def get_products():
    """
    This service has ONLY ONE feature: listing all products.
    """
    return jsonify(PRODUCTS)

if __name__ == '__main__':
    # IMPORTANT: We are running this service on port 5001
    # to keep it separate from our other services.
    print("Product Service running on http://127.0.0.1:5001")
    app.run(host='0.0.0.0', port=5001, debug=True)
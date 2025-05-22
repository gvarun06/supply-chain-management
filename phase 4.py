from flask import Flask, render_template_string

app = Flask(__name__)

# Sample data
suppliers = [
    {"id": "SUP001", "name": "Global Raw Materials", "contact": "contact@grm.com", "location": "New York, USA"}
]

inventory = [
    {"id": "INV101", "product": "Steel Rods", "quantity": 1200, "warehouse": "Warehouse A"}
]

orders = [
    {"id": "ORD2301", "customer": "ABC Manufacturing", "status": "Processing", "date": "2025-05-01"}
]

deliveries = [
    {"id": "DEL5001", "carrier": "FastTrans Logistics", "status": "In Transit", "expected_date": "2025-05-10"}
]

# HTML content embedded (your original HTML)
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Supply Chain Management Dashboard</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }
    h1, h2 { color: #2c3e50; }
    .section { background: #fff; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
    th { background-color: #3498db; color: white; }
  </style>
</head>
<body>

  <h1>Supply Chain Management Dashboard</h1>

  <div class="section">
    <h2>Suppliers</h2>
    <table>
      <tr><th>Supplier ID</th><th>Name</th><th>Contact</th><th>Location</th></tr>
      {% for s in suppliers %}
      <tr><td>{{ s.id }}</td><td>{{ s.name }}</td><td>{{ s.contact }}</td><td>{{ s.location }}</td></tr>
      {% endfor %}
    </table>
  </div>

  <div class="section">
    <h2>Inventory</h2>
    <table>
      <tr><th>Item ID</th><th>Product</th><th>Quantity</th><th>Warehouse</th></tr>
      {% for i in inventory %}
      <tr><td>{{ i.id }}</td><td>{{ i.product }}</td><td>{{ i.quantity }}</td><td>{{ i.warehouse }}</td></tr>
      {% endfor %}
    </table>
  </div>

  <div class="section">
    <h2>Orders</h2>
    <table>
      <tr><th>Order ID</th><th>Customer</th><th>Status</th><th>Date</th></tr>
      {% for o in orders %}
      <tr><td>{{ o.id }}</td><td>{{ o.customer }}</td><td>{{ o.status }}</td><td>{{ o.date }}</td></tr>
      {% endfor %}
    </table>
  </div>

  <div class="section">
    <h2>Deliveries</h2>
    <table>
      <tr><th>Delivery ID</th><th>Carrier</th><th>Status</th><th>Expected Date</th></tr>
      {% for d in deliveries %}
      <tr><td>{{ d.id }}</td><td>{{ d.carrier }}</td><td>{{ d.status }}</td><td>{{ d.expected_date }}</td></tr>
      {% endfor %}
    </table>
  </div>

</body>
</html>
"""

@app.route("/")
def dashboard():
    return render_template_string(
        html_template,
        suppliers=suppliers,
        inventory=inventory,
        orders=orders,
        deliveries=deliveries
    )

if __name__ == "__main__":
    app.run(debug=True)
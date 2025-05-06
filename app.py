from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7223",
    database="Product_Management"
)
cursor = db.cursor(dictionary=True)


@app.route('/')
def index():
    return render_template('index.html')

# Home
@app.route('/index')
def home():
    return render_template('index.html')
# Products
@app.route('/products')
def products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template('products.html', products=products)

@app.route('/products/add', methods=['POST'])
def add_product():
    product_id = request.form['product_id']
    name = request.form['name']
    cursor.execute("INSERT INTO products (product_id, name) VALUES (%s, %s)", (product_id, name))
    db.commit()
    return redirect(url_for('products'))

@app.route('/products/edit', methods=['POST'])
def edit_product():
    product_id = request.form['product_id']
    name = request.form['name']
    cursor.execute("UPDATE products SET name = %s WHERE product_id = %s", (name, product_id))
    db.commit()
    return redirect(url_for('products'))




# Locations
@app.route('/locations')
def locations():
    cursor.execute("SELECT * FROM locations")
    locations = cursor.fetchall()
    return render_template('locations.html', locations=locations)

@app.route('/locations/add', methods=['POST'])
def add_location():
    location_id = request.form['location_id']
    name = request.form['name']
    cursor.execute("INSERT INTO locations (location_id, name) VALUES (%s, %s)", (location_id, name))
    db.commit()
    return redirect(url_for('locations'))

@app.route('/locations/edit', methods=['POST'])
def edit_location():
    location_id = request.form['location_id']
    name = request.form['name']
    cursor.execute("UPDATE locations SET name = %s WHERE location_id = %s", (name, location_id))
    db.commit()
    return redirect(url_for('locations'))




# Movements
@app.route('/movements')
def movements():
    cursor.execute("SELECT * FROM product_movements ORDER BY timestamp DESC")
    movements = cursor.fetchall()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.execute("SELECT * FROM locations")
    locations = cursor.fetchall()
    return render_template('movements.html', movements=movements, products=products, locations=locations)

@app.route('/movements/edit', methods=['POST'])
def edit_movement():
    movement_id = request.form['id']
    product_id = request.form['product_id']
    from_location = request.form.get('from_location') or None
    to_location = request.form.get('to_location') or None
    qty = int(request.form['qty'])
    cursor.execute("""
        UPDATE product_movements 
        SET product_id = %s, from_location = %s, to_location = %s, qty = %s
        WHERE id = %s
    """, (product_id, from_location, to_location, qty, movement_id))
    db.commit()
    return redirect(url_for('movements'))


@app.route('/movements/add', methods=['POST'])
def add_movement():
    product_id = request.form['product_id']
    from_location = request.form.get('from_location') or None
    to_location = request.form.get('to_location') or None
    qty = int(request.form['qty'])
    timestamp = datetime.now()
    cursor.execute("""
        INSERT INTO product_movements (product_id, from_location, to_location, qty, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (product_id, from_location, to_location, qty, timestamp))
    db.commit()
    return redirect(url_for('movements'))

# Report
@app.route('/report')
def report():
    cursor.execute("""
        SELECT 
            p.name AS product_name, 
            l.name AS location_name,
            GREATEST(
                SUM(CASE WHEN pm.to_location = l.location_id THEN qty ELSE 0 END) -
                SUM(CASE WHEN pm.from_location = l.location_id THEN qty ELSE 0 END),
                0
            ) AS qty
        FROM products p
        CROSS JOIN locations l
        LEFT JOIN product_movements pm ON pm.product_id = p.product_id
        GROUP BY p.product_id, l.location_id
        HAVING qty >= 0
    """)
    report = cursor.fetchall()
    return render_template('report.html', report=report)




if __name__ == '__main__':
    app.run(debug=True,port = 8001)

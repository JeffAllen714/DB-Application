from core import app
from flask import redirect, request, render_template
from sqlalchemy.exc import IntegrityError
from models import product, customer, orders, shopping_cart, review

# Routes for Products
@app.route('/products')
def get_products():
    # Retrieve all products from the database
    products = product.get_products()
    # Render the products.html
    return render_template('products.html', products=products)

@app.route('/add_product_form')
def add_product_form():
    # Render the add_product.html
    return render_template('add_product.html')

@app.route('/add_product', methods=["POST"])
def add_product():
    # Retrieve form data from the add_product form
    name = request.form.get("name")
    description = request.form.get("description")
    price = request.form.get("price")
    category = request.form.get("category")
    photo = request.form.get("photo")
    warehouse_id = request.form.get("warehouse_id")
    stock_quantity = request.form.get("stock_quantity")

    try:
        # Call the add_product function from the product model to add a new product to the database
        product.add_product(name, description, price, category, photo, warehouse_id, stock_quantity)
        # Redirect to the products page after adding the product
        return redirect('/products')
    except IntegrityError:
        # Handle the IntegrityError exception
        error_message = "Failed to add the product. Please check the provided details."
        return render_template('error.html', error_message=error_message)

@app.route('/delete_product/<int:id>')
def delete_product(id):
    # Call the delete_product function
    product.delete_product(id)
    # Redirect to the products page
    return redirect('/products')

# Routes for Customers
@app.route('/customers')
def get_customers():
    # Retrieve all customers from the database
    customers = customer.get_customers()
    # Render the customers.html
    return render_template('customers.html', customers=customers)

@app.route('/add_customer_form')
def add_customer_form():
    # Render the add_customer.html
    return render_template('add_customer.html')

@app.route('/add_customer', methods=["POST"])
def add_customer():
    # Retrieve form data from the add_customer form
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    address = request.form.get("address")
    payment_id = request.form.get("payment_id")
    rewards = request.form.get("rewards")
    # Call the add_customer function from the customer model to add a new customer to the database
    customer.add_customer(name, email, password, address, payment_id, rewards)
    # Redirect to the customers page after adding the customer
    return redirect('/customers')

@app.route('/delete_customer/<int:id>')
def delete_customer(id):
    # Call the delete_customer function
    customer.delete_customer(id)
    # Redirect to the customers page
    return redirect('/customers')

# Routes for Orders
@app.route('/orders')
def get_orders():
    # Retrieve all orders from the database
    orders_list = orders.get_orders()
    # Render the orders.html
    return render_template('orders.html', orders=orders_list)

@app.route('/add_order_form')
def add_order_form():
    # Render the add_order.html
    return render_template('add_order.html')

@app.route('/add_order', methods=["POST"])
def add_order():
    # Retrieve form data from the add_order form
    date = request.form.get("date")
    total_amount = request.form.get("total_amount")
    status = request.form.get("status")
    customer_id = request.form.get("customer_id")

    try:
        # Call the add_order function from the orders model to add a new order to the database
        orders.add_order(date, total_amount, status, customer_id)
        # Redirect to the orders page after adding the order
        return redirect('/orders')
    except Exception as e:
        # Handle any exceptions that occur during order addition
        error_message = f"Failed to add the order. Error: {str(e)}"
        return render_template('error.html', error_message=error_message)

@app.route('/delete_order/<int:id>')
def delete_order(id):
    # Call the delete_order function
    orders.delete_order(id)
    # Redirect to the orders page after deleting the order
    return redirect('/orders')

# Routes for Shopping Carts
@app.route('/shopping_carts')
def get_shopping_carts():
    # Retrieve all shopping carts
    shopping_carts = shopping_cart.get_shopping_carts()
    # Render the shopping_carts.html
    return render_template('shopping_carts.html', shopping_carts=shopping_carts)

@app.route('/add_shopping_cart_form')
def add_shopping_cart_form():
    # Render the add_shopping_cart.html
    return render_template('add_shopping_cart.html')

@app.route('/add_shopping_cart', methods=["POST"])
def add_shopping_cart():
    # Retrieve form data from the add_shopping_cart form
    customer_id = request.form.get("customer_id")
    order_id = request.form.get("order_id")
    product_id = request.form.get("product_id")
    cart_group_id = request.form.get("cart_group_id")
    # Call the add_shopping_cart function
    shopping_cart.add_shopping_cart(customer_id, order_id, product_id, cart_group_id)
    # Redirect to the shopping carts page after adding the shopping cart
    return redirect('/shopping_carts')

@app.route('/delete_shopping_cart/<int:id>')
def delete_shopping_cart(id):
    # Call the delete_shopping_cart function
    shopping_cart.delete_shopping_cart(id)
    # Redirect to the shopping carts page after deleting the shopping cart
    return redirect('/shopping_carts')

# Routes for Reviews
@app.route('/reviews')
def get_reviews():
    # Retrieve all reviews from the database
    reviews = review.get_reviews()
    # Render the reviews.html template and pass the reviews data
    return render_template('reviews.html', reviews=reviews)

@app.route('/add_review_form')
def add_review_form():
    # Render the add_review.html
    return render_template('add_review.html')

@app.route('/add_review', methods=["POST"])
def add_review():
    # Retrieve form data from the add_review form
    ratings = request.form.get("ratings")
    comments = request.form.get("comments")
    product_id = request.form.get("product_id")
    customer_id = request.form.get("customer_id")
    # Call the add_review function
    review.add_review(ratings, comments, product_id, customer_id)
    # Redirect to the reviews page after adding the review
    return redirect('/reviews')

@app.route('/delete_review/<int:id>')
def delete_review(id):
    # Call the delete_review function
    review.delete_review(id)
    # Redirect to the reviews page after deleting the review
    return redirect('/reviews')

# Route for Home Page
@app.route('/')
def index():
    # Render the index.html template for the home page
    return render_template('index.html')

# Route for Stylesheet
@app.route('/stylesheet.css')
def stylesheet():
    # Render the stylesheet.css for the different pages
    return render_template('stylesheet.css')

if __name__ == '__main__':
    # debug mode currently enabled
    app.run(port=8000, debug=True)
    
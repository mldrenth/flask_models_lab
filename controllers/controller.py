from flask import render_template
from app import app
from models.orders import orders

@app.route('/')
def index():
    return render_template('index.html', title='Orders', orders = orders)

@app.route('/orders/<index>')
def show_order(index):
    order_index = int(index)
    return render_template('order.html', title = 'Order', order = orders[order_index], order_number = order_index)
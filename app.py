#author -- orsessential
from flask import Flask, request, Response
from database.model import Ordering
from database.db import initialize_db
import json
app = Flask(__name__)
MONGODB_SETTINGS = {
    'host': 'mongodb://localhost/orders'
}
initialize_db(app)

@app.route('/orders')
def get_orders():
    orders = Ordering.objects().to_json()
    return Response(orders, mimetype="application/json", status=200)

@app.route('/orders', methods=['POST'])
def add_order():
    body = request.get_json()
    order =  Ordering(**body).save()
    id = order.id
    return {'id': str(id)}, 200

@app.route('/orders/<id>', methods=['PUT'])
def update_order(id):
    body = request.get_json()
    try:
        Ordering.objects.get(id=id).update(**body)
        return f"order id : {id} has been updated", 200
    except:
        return f"order id : {id} or item not match", 204

@app.route('/orders/<id>', methods=['DELETE'])
def delete_order(id):
    try: 
        order = Ordering.objects.get(id=id).delete()
        return Response(order, mimetype="application/json", status=200)
    except:
        return f"order id : {id} not found", 204

@app.route('/orders/<id>')
def get_order(id):
    try:
        orders = Ordering.objects.get(id=id).to_json()
        return Response(orders, mimetype="application/json", status=200)
    except:
        return f"order id : {id} not found", 204

@app.route('/orders/<id>', methods=['PATCH'])
def update_order_item(id):
    data = request.json
    try:
        Ordering.objects.get(id=id).update(**data)
        return f"item id : {id} has been updated", 200
    except:
        return f"order id : {id} not found", 204

app.run()


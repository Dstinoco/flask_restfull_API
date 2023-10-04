from flask import Flask, jsonify, request

app = Flask(__name__)

purchase_orders = [
    {
        "id": 1,
        "description": "Pedido de compra 1",
        "items": [
            {
                'id': 1,
                "description": "Item do pedido 1",
                "price": 20.99
            }
        ]
    }
]




@app.route('/')
def home():
    return("<h1>API Online</h1>")

@app.route('/purchase')
def get_purchase_orders():
    return jsonify(purchase_orders)


@app.route("/purchase/<int:id>")
def purchase_orders_by_id(id):
   for item in purchase_orders:
       if item.get("id") == id:
           return jsonify(item)
       else:
           return jsonify({"message": "Item não encontrado"})

@app.route("/purchase", methods=['POST'])
def create_purchase():
    request_data = request.get_json()
    purchase_order = {
        "id": request_data['id'],
        "description": request_data['description'],
        "items":[]
    }

    purchase_orders.append(purchase_order)
    return jsonify({"message": f"Item adicionado com sucesso! {purchase_order}"})



@app.route('/purchase/<int:id>/items')
def get_purchase_items(id):
    for item in purchase_orders:
        if item.get('id') == id:
            return jsonify(item["items"])
        return jsonify({"message": 'item nao encontrado'})
    

@app.route('/purchase/<int:id>/items', methods=['POST'])
def create_purchase_items(id):
    req_data = request.get_json()
    for item in purchase_orders:
        if item.get('id') == id:
            item['items'].append({
                "id": req_data['id'],
                "description": req_data['description'],
                "price": req_data["price"]
            })
            return jsonify({"message": "Item adicionado com sucesso!"})
    return jsonify({"message": 'item nao encontrado'})    







app.run(debug=True)
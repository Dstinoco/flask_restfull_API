from flask import Flask, jsonify
from flask_restful import Api, Resource
from purchase.routes import PurchaseOrders

app = Flask(__name__)
api = Api(app)

    

api.add_resource(PurchaseOrders, '/purchase')    




app.run(debug=True)
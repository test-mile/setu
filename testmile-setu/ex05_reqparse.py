from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import login, identify

app = Flask(__name__)
api = Api(app)
app.secret_key = 'rahul'
jwt = JWT(app, login, identify) # /auth endpoint

items = []

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('name', 
		type=str, 
		required=True, 
		help='Name of item. String. Can not be blank.'
	)
	parser.add_argument('price', 
		type=float, 
		required=True, 
		help='Price of item. Number. Can not be blank.'
	)

	def __get_item_if_exists(self, name):
		return next(iter(filter(lambda x: x['name'] == name, items)), None)

	# No need to add explcit Flask @app.route, It is done as a part of resource registration
	@jwt_required()
	def get(self, name):
		item = self.__get_item_if_exists(name)
		return {'item' : item}, item and 200 or 404

	def post(self):
		rdata = Item.parser.parse_args()	# all other data is ignored.
		name = rdata['name']
		item = self.__get_item_if_exists(name)
		if item:
			return {'code' : 'error', 'message' : 'item already exists for name: '  + name}, 400 # Bad Request
		item = {'name' : name, 'price' : rdata['price']}
		items.append(item)
		return {'code' : 'success'}, 201

	def delete(self, name):
		global items
		items = list(filter(lambda x: x['name'] != name, items))
		return {'code' : 'success'}

	def put(self):
		rdata = Item.parser.parse_args()	# all other data is ignored.
		name = rdata['name']
		item = self.__get_item_if_exists(name)
		if item:
			item.update(rdata)
			return {'code' : 'success'}, 200
		else:
			item = {'name' : name, 'price' : rdata['price']}
			items.append(item)
			return {'code' : 'success'}, 201

class ItemList(Resource):
	def get(self):
		return {'items' : items}

api.add_resource(Item, '/item', '/item/<string:name>', endpoint='item')
api.add_resource(ItemList, '/items', endpoint='items')
app.run(port=9005, debug=True)


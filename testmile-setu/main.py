from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):

	def __get_item_if_exists(self, name):
		return next(iter(filter(lambda x: x['name'] == name, items)), None)

	def get(self, name):
		item = self.__get_item_if_exists(name)
		return {'item' : item}, item and 200 or 404

	def post(self):
		rdata = request.get_json() #force=True -> now it does not need content-type header
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
		rdata = request.get_json()
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
app.run(port=9898, debug=True)
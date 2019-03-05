from flask import Flask, request
from flask_restful import Resource, Api

from setu.interface.setu import SetuSvc

from setu.core.config.processor import ConfigCreator
ConfigCreator.init()

app = Flask(__name__)
api = Api(app)



api.add_resource(SetuSvc, '/setu', endpoint='setu')

# api.add_resource(ItemList, '/items', endpoint='items')
app.run(port=9000, debug=True, use_evalex=False)
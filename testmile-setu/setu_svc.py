from flask import Flask, request
from flask_restful import Resource, Api
from setu.interface.guiauto import *

app = Flask(__name__)
api = Api(app)

# api.add_resource(Item, '/guiauto/launch/automator', '/item/<string:name>', endpoint='item')
api.add_resource(AutomatorLauncher, '/guiauto/automator/launch', endpoint='guiauto_launch')
api.add_resource(AutomatorQuitter, '/guiauto/automator/quit', endpoint='guiauto_quit')
api.add_resource(AutomatorActionSvc, '/guiauto/automator/action', endpoint='guiauto_action')
api.add_resource(ElementActionSvc, '/guiauto/element/action', endpoint='guielem_action')
api.add_resource(MultiElementActionSvc, '/guiauto/multielement/action', endpoint='guimultielem_action')
api.add_resource(DropDownActionSvc, '/guiauto/dropdown/action', endpoint='dropdown_action')
api.add_resource(RadioGroupActionSvc, '/guiauto/radiogroup/action', endpoint='radiogroup_action')
api.add_resource(FrameActionSvc, '/guiauto/frame/action', endpoint='frame_action')
api.add_resource(WindowActionSvc, '/guiauto/window/action', endpoint='window_action')
api.add_resource(AlertActionSvc, '/guiauto/alert/action', endpoint='alert_action')
# api.add_resource(ItemList, '/items', endpoint='items')
app.run(port=9000, debug=True)
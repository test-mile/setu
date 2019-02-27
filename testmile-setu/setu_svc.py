from flask import Flask, request
from flask_restful import Resource, Api
from setu.interface.guiauto import *

app = Flask(__name__)
api = Api(app)

# api.add_resource(Item, '/guiauto/launch/automator', '/item/<string:name>', endpoint='item')
api.add_resource(AutomatorLauncher, '/guiautomator/launch', endpoint='guiauto_launch')
api.add_resource(AutomatorQuitter, '/guiautomator/quit', endpoint='guiauto_quit')
api.add_resource(AutomatorActionSvc, '/guiautomator/action', endpoint='guiauto_action')
api.add_resource(ElementActionSvc, '/guiautomator/element/action', endpoint='guielem_action')
api.add_resource(MultiElementActionSvc, '/guiautomator/multielement/action', endpoint='guimultielem_action')
api.add_resource(DropDownActionSvc, '/guiautomator/dropdown/action', endpoint='dropdown_action')
api.add_resource(RadioGroupActionSvc, '/guiautomator/radiogroup/action', endpoint='radiogroup_action')
api.add_resource(FrameActionSvc, '/guiautomator/frame/action', endpoint='frame_action')
api.add_resource(WindowActionSvc, '/guiautomator/window/action', endpoint='window_action')
api.add_resource(AlertActionSvc, '/guiautomator/alert/action', endpoint='alert_action')
# api.add_resource(ItemList, '/items', endpoint='items')
app.run(port=9000, debug=True)
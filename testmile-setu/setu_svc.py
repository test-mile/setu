from flask import Flask, request
from flask_restful import Resource, Api
from setu.interface.guiauto import *
from setu.interface.testsession import *

from setu.core.config.processor import ConfigCreator
ConfigCreator.init()

app = Flask(__name__)
api = Api(app)

api.add_resource(TestSessionInitSvc, '/testsession/init', endpoint='testsession_init')
api.add_resource(TestSessionFinishSvc, '/testsession/finish', endpoint='testsession_finish')
api.add_resource(TestSessionActionSvc, '/testsession/action', endpoint='testsession_action')
api.add_resource(TestSessionConfActionSvc, '/testsession/conf/action', endpoint='conf_action')
api.add_resource(TestSessionDataSourceActionSvc, '/testsession/datasource/action', endpoint='datasource_action')
api.add_resource(AutomatorLauncher, '/testsession/guiauto/automator/launch', endpoint='guiauto_launch')
api.add_resource(AutomatorQuitter, '/testsession/guiauto/automator/quit', endpoint='guiauto_quit')
api.add_resource(AutomatorActionSvc, '/testsession/guiauto/automator/action', endpoint='guiauto_action')
api.add_resource(ElementActionSvc, '/testsession/guiauto/element/action', endpoint='guielem_action')
api.add_resource(MultiElementActionSvc, '/testsession/guiauto/multielement/action', endpoint='guimultielem_action')
api.add_resource(DropDownActionSvc, '/testsession/guiauto/dropdown/action', endpoint='dropdown_action')
api.add_resource(RadioGroupActionSvc, '/testsession/guiauto/radiogroup/action', endpoint='radiogroup_action')
api.add_resource(FrameActionSvc, '/testsession/guiauto/frame/action', endpoint='frame_action')
api.add_resource(WindowActionSvc, '/testsession/guiauto/window/action', endpoint='window_action')
api.add_resource(AlertActionSvc, '/testsession/guiauto/alert/action', endpoint='alert_action')
# api.add_resource(ItemList, '/items', endpoint='items')
app.run(port=9000, debug=True, use_evalex=False)
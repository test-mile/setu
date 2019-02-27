from flask import request
from flask_restful import Resource
from .objmgr import SetuSvcObjectManager
from .guiautmator_handler import GuiAutomatorHandler
from setu.core.config.ex import EX_CONFIG

_GUI_AUTOMATORS = {}

class AutomatorLauncher(Resource):

    def post(self):
        handler = GuiAutomatorHandler()
        handler.launch_automator(EX_CONFIG)#request.get_json(force=True))
        SetuSvcObjectManager.register_gui_automator_handler(handler)
        return {'result' : 'success', 'responseData': {'automatorSetuId' : handler.setu_id}}, 200

def get_handler(json_dict):
    return SetuSvcObjectManager.get_gui_automator_handler(json_dict["args"]["automatorSetuId"])

class AutomatorQuitter(Resource):

    def post(self):
        handler = get_handler(request.get_json(force=True))
        handler.quit()
        SetuSvcObjectManager.deregister_gui_automator_handler(handler)
        return {'result' : 'success'}, 200

class AutomatorActionSvc(Resource):

    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_handler(json_dict)
            del json_dict["args"]["automatorSetuId"]
            output = getattr(handler, json_dict["action"].lower())(**json_dict["args"])
            return {'result' : 'success', 'responseData':output}, 200
        except Exception as e:
            print(e)
            import traceback
            return {
                'result' : 'ERROR',
                'emessage' : str(e),
                'etrace' : traceback.format_exc()
            }, 500

class ElementActionSvc(Resource):

    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_handler(json_dict)
            del json_dict["args"]["automatorSetuId"]
            elem_setu_id = json_dict["args"]["elementSetuId"]
            del json_dict["args"]["elementSetuId"]
            output = handler.take_element_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])
            return {'result' : 'success', 'responseData':output}, 200
        except Exception as e:
            print(e)
            import traceback
            return {
                'result' : 'ERROR',
                'emessage' : str(e),
                'etrace' : traceback.format_exc()
            }, 500


class MultiElementActionSvc(Resource):

    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_handler(json_dict)
            del json_dict["args"]["automatorSetuId"]
            elem_setu_id = json_dict["args"]["elementSetuId"]
            del json_dict["args"]["elementSetuId"]
            output = handler.take_multielement_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])
            return {'result' : 'success', 'responseData':output}, 200
        except Exception as e:
            print(e)
            import traceback
            return {
                'result' : 'ERROR',
                'emessage' : str(e),
                'etrace' : traceback.format_exc()
            }, 500

class DropDownActionSvc(Resource):

    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_handler(json_dict)
            del json_dict["args"]["automatorSetuId"]
            elem_setu_id = json_dict["args"]["elementSetuId"]
            del json_dict["args"]["elementSetuId"]
            output = handler.take_dropdown_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])
            return {'result' : 'success', 'responseData':output}, 200
        except Exception as e:
            print(e)
            import traceback
            return {
                'result' : 'ERROR',
                'emessage' : str(e),
                'etrace' : traceback.format_exc()
            }, 500

class RadioGroupActionSvc(Resource):

    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_handler(json_dict)
            del json_dict["args"]["automatorSetuId"]
            elem_setu_id = json_dict["args"]["elementSetuId"]
            del json_dict["args"]["elementSetuId"]
            output = handler.take_radiogroup_action(json_dict["action"].lower(), elem_setu_id, json_dict["args"])
            return {'result' : 'success', 'responseData':output}, 200
        except Exception as e:
            print(e)
            import traceback
            return {
                'result' : 'ERROR',
                'emessage' : str(e),
                'etrace' : traceback.format_exc()
            }, 500
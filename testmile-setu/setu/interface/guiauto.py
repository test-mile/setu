from flask import request
from flask_restful import Resource
from .objmgr import SetuSvcObjectManager
from .guiautomator_handler import GuiAutomatorHandler

_GUI_AUTOMATORS = {}

def get_testsession_handler(json_dict):
    handler = SetuSvcObjectManager.get_testsession_handler(json_dict["args"]["testSessionSetuId"])
    del json_dict["args"]["testSessionSetuId"]
    return handler

class AutomatorLauncher(Resource):

    def post(self):
        json_dict = request.get_json(force=True)
        handler = get_testsession_handler(json_dict)
        res = handler.launch_automator(json_dict)
        return {'result' : 'success', 'responseData': res}, 200

class AutomatorQuitter(Resource):

    def post(self):
        json_dict = request.get_json(force=True)
        handler = get_testsession_handler(json_dict)
        handler.quit_automator(json_dict)
        return {'result' : 'success'}, 200

class AutomatorActionSvc(Resource):

    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_testsession_handler(json_dict)
            res = handler.take_automator_action(json_dict)
            return {'result' : 'success', 'responseData': res}, 200
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
            handler = get_testsession_handler(json_dict)
            res = handler.take_element_action(json_dict)
            return {'result' : 'success', 'responseData': res}, 200
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
            handler = get_testsession_handler(json_dict)
            res = handler.take_multielement_action(json_dict)
            return {'result' : 'success', 'responseData': res}, 200
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
            handler = get_testsession_handler(json_dict)
            res = handler.take_dropdown_action(json_dict)
            return {'result' : 'success', 'responseData': res}, 200
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
            handler = get_testsession_handler(json_dict)
            res = handler.take_radiogroup_action(json_dict)
            return {'result' : 'success', 'responseData': res}, 200
        except Exception as e:
            print(e)
            import traceback
            return {
                'result' : 'ERROR',
                'emessage' : str(e),
                'etrace' : traceback.format_exc()
            }, 500

class FrameActionSvc(Resource):

    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_testsession_handler(json_dict)
            res = handler.take_frame_action(json_dict)
            return {'result' : 'success', 'responseData': res}, 200
        except Exception as e:
            print(e)
            import traceback
            return {
                'result' : 'ERROR',
                'emessage' : str(e),
                'etrace' : traceback.format_exc()
            }, 500


class WindowActionSvc(Resource):

    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_testsession_handler(json_dict)
            res = handler.take_window_action(json_dict)
            return {'result' : 'success', 'responseData': res}, 200
        except Exception as e:
            print(e)
            import traceback
            return {
                'result' : 'ERROR',
                'emessage' : str(e),
                'etrace' : traceback.format_exc()
            }, 500


class AlertActionSvc(Resource):

    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_testsession_handler(json_dict)
            res = handler.take_alert_action(json_dict)
            return {'result' : 'success', 'responseData': res}, 200
        except Exception as e:
            print(e)
            import traceback
            return {
                'result' : 'ERROR',
                'emessage' : str(e),
                'etrace' : traceback.format_exc()
            }, 500
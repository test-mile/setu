from flask import request
from flask_restful import Resource
from .objmgr import SetuSvcObjectManager
from .testsession_handler import TestSessionHandler

class TestSessionInitSvc(Resource):

    def post(self):
        handler = TestSessionHandler()
        json_dict = request.get_json(force=True)
        root_dir = json_dict["args"]["rootDir"]
        config_id = handler.init(root_dir)
        SetuSvcObjectManager.register_testsession_handler(handler)
        resData = {
            'testSessionSetuId' : handler.setu_id,
            'configSetuId' : config_id
        }
        return {'result' : 'success', 'responseData': resData}, 200

def get_handler(json_dict):
    return SetuSvcObjectManager.get_testsession_handler(json_dict["args"]["testSessionSetuId"])

class TestSessionFinishSvc(Resource):

    def post(self):
        handler = get_handler(request.get_json(force=True))
        handler.quit()
        SetuSvcObjectManager.deregister_testsession_handler(handler)
        return {'result' : 'success'}, 200

class TestSessionActionSvc(Resource):
    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_handler(json_dict)
            del json_dict["args"]["testSessionSetuId"]
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


class TestSessionConfActionSvc(Resource):
    def post(self):
        try:
            json_dict = request.get_json(force=True)
            handler = get_handler(json_dict)
            del json_dict["args"]["testSessionSetuId"]
            output = handler.take_conf_action(json_dict)
            return {'result' : 'success', 'responseData': output}, 200
        except Exception as e:
            print(e)
            import traceback
            return {
                'result' : 'ERROR',
                'emessage' : str(e),
                'etrace' : traceback.format_exc()
            }, 500 
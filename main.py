import json, falcon

class ObjRequestClass:
    def on_get(self, req, res):
        content = {
            'name' : 'Aakriti',
            'age' : '22',
            'country' : 'India'
        }
        res.body = json.dumps(content)


api = falcon.API()

api.add_route('/test', ObjRequestClass())


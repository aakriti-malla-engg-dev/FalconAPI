import falcon
import json

from db_client import *


class NoteResource:

    def on_get(self, req, resp):
        if req.get_param("id"):
            result = {'note': rdb.db(PROJECT_DB).table(PROJECT_TABLE).get(req.get_param("id")).run(db_connection)}
        else:
            note_cursor = rdb.db(PROJECT_DB).table(PROJECT_TABLE).run(db_connection)
            result = {'notes': [i for i in note_cursor]}
        resp.body = json.dumps(result)

    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)

        try:
            result = json.loads(raw_json, encoding='utf-8')
            sid = rdb.db(PROJECT_DB).table(PROJECT_TABLE).insert(
                {'title': result['title'], 'body': result['body']}).run(
                db_connection)
            resp.body = 'Successfully inserted %s' % sid
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON',
                                   'Could not decode the request body. The ''JSON was incorrect.')


api = falcon.API()
api.add_route('/notes', NoteResource())

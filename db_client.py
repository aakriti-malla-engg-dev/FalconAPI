import os
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
rdb = r.RethinkDB()

RDB_HOST = 'localhost'
RDB_PORT = 28015

PROJECT_DB = 'todo'
PROJECT_TABLE = 'notes'

db_connection = rdb.connect(RDB_HOST, RDB_PORT)


def dbSetup():
    try:
        rdb.db_create(PROJECT_DB).run(db_connection)
        print('Database setup completed.')
    except RqlRuntimeError:
        try:
            rdb.db(PROJECT_DB).table_create(PROJECT_TABLE).run(db_connection)
            print('Table creation completed')
        except:
            print('Table already exists.Nothing to do')


dbSetup()

# import rethinkdb as r
# from rethinkdb.errors import RqlRuntimeError
#
# rdb = r.RethinkDB()
# PROJECT_DB = 'todo'
# PROJECT_TABLE = 'notes'
# if __name__ == "__main__":
#     conn = rdb.connect(host='127.0.0.1', port='28015',db=PROJECT_DB)
#     try:
#         cursor = rdb.table(PROJECT_TABLE).run(conn)
#         for record in cursor:
#             print(record)
#     except RqlRuntimeError as err:
#         print(err.message)
#     finally:
#         conn.close()


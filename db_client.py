import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError

RDB_HOST = 'localhost'
RDB_PORT = 29015

PROJECT_DB = 'todo'
PROJECT_TABLE = 'notes'

rdb = r.RethinkDB()
db_connection = rdb.connect(RDB_HOST, RDB_PORT)


def dbSetup():
    try:
        r.db_create(PROJECT_DB).run(db_connection)
        print("Database setup completed.")
    except RqlRuntimeError:
        try:
            r.db(PROJECT_DB).table_create(PROJECT_TABLE).run(db_connection)
            print("Table creation completed")
        except:
            print("Table already exists.Nothing to do")


dbSetup()

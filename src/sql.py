import sqlite3
import main
from contextlib import closing

class DBconnect:
    def __init__(self, dbname):
        self.dbname = dbname

    def creat_database(self):
        conn = sqlite3.connect(self.dbname)
        # create table
        create_table = '''create table if not exists cowrie
            (
                id INTEGER PRIMARY KEY,
                eventid TEXT,
                ttylog TEXT,
                timestamp TEXT,
                message TEXT,
                isError INTEGER,
                src_ip TEXT,
                session TEXT,
                sensor TEXT
            )'''
        conn.execute(create_table)
        conn.commit()

    def update_database(self, log):
        with closing(sqlite3.connect(self.dbname)) as conn:
            c = conn.cursor()
            sql = 'insert into cowrie (id, eventid, ttylog, timestamp, message, isError, src_ip, session, sensor) values (?,?,?,?,?,?,?,?,?)'
            c.execute(sql, log)
            conn.commit()

    def show_database(self):
        with closing(sqlite3.connect(self.dbname)) as conn:
            c = conn.cursor()
            select_sql = 'select * from cowrie'
            for row in c.execute(select_sql):
                print(row)

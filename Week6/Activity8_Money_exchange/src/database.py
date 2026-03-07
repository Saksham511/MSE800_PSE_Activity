import sqlite3
class db():
    def __init__(self, db_file='Money_Exchange_rate.db'):
        self.conn=sqlite3.connect(db_file)
        self.cursor=self.conn.cursor
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Exchange_rates (
                            id PRIMARY KEY ,
                            detail TEXT NOT NULL,
                            rate REAL NOT NULL)""")
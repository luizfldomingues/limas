import sqlite3
import os

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        def new_database():
            with open('database/limas.sql', 'r') as sql_file:
                sql_script = sql_file.read()
                with sqlite3.connect(self.db_path) as con:
                    cur = con.cursor()
                    cur.executescript(sql_script)
                    con.commit()
                    print("Novo banco de dados criado com sucesso")
        if not os.path.isfile(self.db_path):
            new_database()

Database("database/limas.db")


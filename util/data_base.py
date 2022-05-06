import re
import sqlite3

class DataBase():
    def __init__(self):
        #sqlite3 connection
        self.con = sqlite3.connect('main_database.db')
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    #sqlite3 data outputs and inputs
    def dataRequest(self, request):
        with self.con:
            self.cur.execute(request)
            self.cur.close
        
    def dataPull(self, request):
        with self.con:
            self.cur.execute(request)
            self.cur.close
            return self.cur.fetchone()

    def dataPullAll(self):
        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("SELECT * FROM users WHERE id = 1")
            result = [dict(row) for row in self.cur.fetchall()]
            for i in result:
                print(i)

    def insert(self, id):
        with self.con:
            self.cur.execute(f'''
            INSERT INTO blueGem(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO boots(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO chest(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO greenGem(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO helmet(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO inventory(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO pants(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO redGem(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO enemy1(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO enemy2(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO enemy3(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO enemy4(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO enemy5(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO enemy6(id) VALUES({id})
            ''')
            self.cur.execute(f'''
            INSERT INTO stats(id) VALUES({id})
            ''')
            self.cur.close()

import sqlite3

class DataBase():
    def __init__(self):
        #sqlite3 connection
        self.con = sqlite3.connect('mainData.db')
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

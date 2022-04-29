import sqlite3

#sqlite3 connection
con = sqlite3.connect('mainData.db')
cur = con.cursor()

#sqlite3 data outputs and inputs
def dataRequest(request):
    with con:
        cur.execute(request)
        cur.close
    
def dataPull(request):
    with con:
        cur.execute(request)
        cur.close
        return cur.fetchone()

import sqlite3
import threading
import time

def readdata():
    conn = sqlite3.connect('Database_Order.db')
    cr = conn.cursor()
    while True:
        cr.execute('SELECT * FROM INVOICE WHERE status = 0')
        rows = cr.fetchall()
        if len(rows) > 0:
            print(rows)
        time.sleep(1)
    conn.close()


t1 = threading.Thread(target=readdata)
t1.start()

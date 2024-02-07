import sqlite3
import threading
import time
import sqlite3
import pyttsx3

engine = pyttsx3.init()
def eng_audio(text):
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()


def check_new_orders():
    conn = sqlite3.connect('Database_Order.db')
    cr = conn.cursor()
    cr.execute("SELECT MAX(ID) FROM INVOICE")
    result = cr.fetchone()
    prev_last_id = result[0]
    while True:
        cr.execute("SELECT MAX(ID) FROM INVOICE")
        result = cr.fetchone()
        curr_last_id = result[0]
        if curr_last_id != prev_last_id:
            cr.execute(f'SELECT * FROM INVOICE WHERE ID={curr_last_id}')
            row = cr.fetchall()
            for rows in row:
                txt1 = "Table 1 Ordered {} {}".format(round(rows[2]), rows[1])
                eng_audio(txt1)
                order_details = "ITEM: " + str(rows[1]) + "\nQuantity: " + str(rows[2])
                print("ITEM: " + str(rows[1]) + "\nQuantity: " + str(rows[2]))
                print("Done!")
                print()
            prev_last_id = curr_last_id
    conn.close()

thread = threading.Thread(target=check_new_orders)
thread.start()


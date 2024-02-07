#Module
import sqlite3
import speech_recognition as sr
import pyttsx3
conn = sqlite3.connect('Database_Items.db')
cursor = conn.cursor()
# conn.execute('''CREATE TABLE ITEMS
#              (ID INTEGER PRIMARY KEY AUTOINCREMENT,
#              Items VARCHAR(50),
#              Price FLOAT)''')

#Function
def Add_Items():
    print("Enter Item Name and Price: ")
    item, price = input().split()
    conn.execute("INSERT INTO ITEMS('Items', 'Price') VALUES (?, ?);", (item, price))
    conn.commit()
def Update_Items():
    print("Enter the Item Name to update: ")
    item = input() 
    print("Enter the Update Price: ")
    price = input()
    sql = 'UPDATE ITEMS SET Price=? WHERE Items=?;'
    cursor.execute(sql, (price, item, ))
    conn.commit() 
def Delete_Items():
    print("Enter the Item Name to delete: ")
    item = input()
    sql = 'DELETE FROM ITEMS WHERE Items=?;'
    cursor.execute(sql, (item,))
    conn.commit()
def Display_Items():
    cursor.execute('SELECT * FROM ITEMS')
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print('+------+-----------+---------+')
    print('|  ID  |   ITEMS   |  PRICE  |')
    print('+------+-----------+---------+')
    for row in rows:
            print("|  {}  |     {}    |    {}   |".format(row[0], row[1], row[2]))

#User Input
while(True):
    print("1.Add\n2.Update\n3.Delete\n4.Display\nEnter Your Choice: ")
    n = int(input())
    if n == 1:
        Add_Items()
    elif(n == 2):
        Update_Items()
    elif(n == 3):
        Delete_Items()
    else:
        Display_Items()
    print("Do you want to continue (Y/N): ")
    q = input()
    if(q == 'N'):
        break
 
conn.commit()
conn.close()
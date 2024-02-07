import sqlite3
conn = sqlite3.connect('Database_Order.db')
cursor = conn.cursor()
# conn.execute('''CREATE TABLE INVOICE
#              (ID INTEGER,
#              ITEMS VARCHAR(50),
#              QUANTITY FLOAT)''')

# cursor.execute('DELETE FROM `sqlite_sequence` WHERE `name` = "INVOICE";')

# cursor.execute('DELETE FROM INVOICE WHERE ITEMS = "Idli";')

# cursor.execute('UPDATE INVOICE SET FLAG = 1')
cursor.execute('SELECT * FROM INVOICE;')
# conn.execute("INSERT INTO INVOICE('ID', 'Items', 'Quantity') VALUES (?, ?, ?);", (1, "Idli", 2))
# conn.execute("INSERT INTO INVOICE('ID', 'Items', 'Quantity') VALUES (?, ?, ?);", (1, "Dosa", 3))

rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]
print('+-------+-----------+------------+')
print('|  ID   |  ITEMS   |  QUANTITY  |')
print('+-------+-----------+------------+')
for row in rows:
    print("|  {}  |     {}    |    {}   |".format(row[0], row[1], row[2]))
# # print(cursor.lastrowid)
# cursor.execute("SELECT MAX(ID) FROM INVOICE")

# result = cursor.fetchone()

# # if result[0] is not None:
# last_id = result[0]
# print("Last ID value:", last_id)
# # else:
#     # print("No IDs found in the table.")
conn.commit()
conn.close()

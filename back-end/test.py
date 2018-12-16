import sqlite3

conn = sqlite3.connect('movieshop.db')
cursor = conn.cursor()

cursor.execute('select * from cart')
print(cursor.fetchall())
cursor.close()
from pyhive import hive

cursor = hive.connect(host='localhost', port='10000').cursor()

cursor.execute('select * from movies')
print(cursor.fetchall())

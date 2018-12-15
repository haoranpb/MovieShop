from pyhive import hive

cursor = hive.connect(host='localhost', port='10000').cursor()

# cursor.execute('CREATE TABLE Movies(id STRING, title STRING, actor STRING, director STRING, \
#                 date STRING, price STRING, genre STRING, review STRING);')
cursor.execute('select * from pokes')
print(cursor.fetchall())
# data = pd.DataFrame(cursor.fetchall())
# print(data.head())

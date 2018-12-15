from pyhive import hive

cursor = hive.connect(host='localhost', port='10000').cursor()

cursor.execute('drop table movies')
cursor.execute('CREATE TABLE movies(id STRING, title STRING, actor STRING, director STRING, \
                time STRING, price FLOAT, genre STRING, review INT)')


# print(cursor.fetchall())
# data = pd.DataFrame(cursor.fetchall())
# print(data.head())

from pymongo import MongoClient

client = MongoClient()

db = client['movie']

collection = db['cart']

document = {
    'id': '123456',
    'title': 'cart',
    'actor': 'ludanxer',
    'director': 'lucass',
    'time': '2018',
    'price': 29.99,
    'genre': 'Action',
    'review': 10
}
collection.insert_one(document)

# cursor = hive.connect(host='localhost', port='10000').cursor()
# conn = sqlite3.connect('movieshop.db')
# cursor = conn.cursor()

# cursor.execute('create table cart(id varchar(50), title varchar(50), actor varchar(50), director varchar(50), \
#                 time varchar(50), price float, genre varchar(50), review int)')
# cursor.close()

# cursor.execute('drop table cart')
# cursor.execute("CREATE TABLE cart(id STRING primary key, title STRING, actor STRING, director STRING, \
#                 time STRING, price FLOAT, genre STRING, review INT)")

# print(cursor.fetchall())
# data = pd.DataFrame(cursor.fetchall())
# print(data.head())

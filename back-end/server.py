"""
    Micro Server For Movie Shop
"""
import json
from pymongo import MongoClient
import time
from flask import request, Flask
from pyhive import hive

cursor = hive.connect(host='localhost', port='10000').cursor()
client = MongoClient()
db = client['movie']
cart = db['cart']
member = db['member']

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def sign_up():
    document = {
        'usr': request.form['usr'],
        'pwd': request.form['pwd']
    }
    member.insert_one(document)
    return '200'

@app.route('/signin', methods=['POST'])
def sign_in():
    result_filter = {
        'usr': request.form['usr'],
        'pwd': request.form['pwd']
    }
    result = member.find_one(result_filter)
    if result:
        return 'True'
    else:
        return 'False'


def search_movie(genre, low, high, title, year, start, number):
    json_body = {}

    cursor.execute("select * from movies where genre='%s' and time like '%s' and \
        title like '%s' and price between %.2f and %.2f \
        limit %d" % (genre, year, title, low, high, number))
    result = cursor.fetchall()
    i = 0
    for movie in result:
        child = {}
        (child['id'], child['title'], child['actor'], child['director'], child['time'],
        child['price'], child['genre'], child['review']) = movie
        json_body[i] = child
        i += 1
    end_time = time.time()
    json_body['time'] = round(end_time - start, 2)
    json_body['number'] = i
    return json.dumps(json_body, indent=2)

@app.route('/search', methods=['GET', 'POST'])
def search():
    start_time = time.time()
    genre = request.args.get('genre')
    number = int(request.args.get('number'))
    low_price = 0.0
    high_price = 40.0
    title = '%'
    year = '%'
    if 'low' in request.args:
        low_price = float(request.args.get('low'))
    if 'high' in request.args:
        high_price = float(request.args.get('high'))
    if 'name' in request.args:
        title = '%' + request.args.get('name') + '%'
    if 'year' in request.args:
        year = request.args.get('year') + '%'

    print(genre, low_price, high_price, title, year, number)
    result = search_movie(genre, low_price, high_price, title, year, start_time, number)
    return result

@app.route('/addcart', methods=['GET', 'POST'])
def add_cart():
    document = {
        'id': request.args.get('id'),
        'title': request.args.get('title'),
        'actor': request.args.get('actor'),
        'director': request.args.get('director'),
        'time': request.args.get('time'),
        'price': float(request.args.get('price')),
        'genre': request.args.get('genre'),
        'review': int(request.args.get('review'))
    }
    cart.insert_one(document)
    return '200'

@app.route('/deletecart', methods=['GET', 'POST'])
def delete_cart():
    movie_id = request.args.get('id')
    cart.delete_one({'id': movie_id})
    return '200'

@app.route('/getcart', methods=['GET', 'POST'])
def get_cart():
    i = 0
    json_body = {}
    for item in cart.find():
        json_body[i] = item
        json_body[i].pop('_id')
        i += 1
    return json.dumps(json_body, indent=2)

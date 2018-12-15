"""
    Micro Server For Movie Shop
"""
import json
from flask import request
from flask import Flask
from pyhive import hive
import time

cursor = hive.connect(host='localhost', port='10000').cursor()

app = Flask(__name__)

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

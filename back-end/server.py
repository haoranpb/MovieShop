"""
    Micro Server For Movie Shop
"""
import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def search():
    genre = request.args.get('genre')
    low_price = request.args.get('low')
    high_price = request.args.get('high')

    json_body = {
        'id': 17213,
        'data': {
            'movie': 'hello world',
            'genre': request.args.get('genre')
        }
    }
    return json.dumps(json_body, indent=2)

def search_db():
    return {}
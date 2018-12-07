from book_parser import BookParser
from flask import Flask, jsonify, request, abort
import redis
import json

# Flask configuration
app = Flask(__name__)

#Redis configuration
redis_host = "localhost"
redis_port = 6379
redis_password = ""

redisServer = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

@app.route('/api/books', methods=['GET'])
def get_book_rating():
    book_name = request.args.get('name')
    if redisServer.exists(book_name):
        redis_search = redisServer.get(book_name)
        print(redis_search)
        search_result = json.loads(redis_search)
        return jsonify(search_result)
    book_parser = BookParser(book_name)
    book_parser.parse_pages()
    result_names = book_parser.get_result_names()
    ratings = book_parser.get_ratings()
    if ratings:
        search_result = {'names':  result_names, 'ratings': ratings}
        json_result = json.dumps(search_result)
        redisServer.set(book_name, json_result)
        return jsonify(search_result)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
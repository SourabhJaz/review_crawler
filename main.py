from book_parser import BookParser
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/api/books', methods=['GET'])
def get_book_rating():
    book_name = request.args.get('name')
    print(book_name)
    book_parser = BookParser(book_name)
    book_parser.parse_pages()
    result_names = book_parser.get_result_names()
    ratings = book_parser.get_ratings()
    if ratings:
        return jsonify({'names': result_names, 'ratings': ratings})
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
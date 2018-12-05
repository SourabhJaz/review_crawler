from book_parser import BookParser
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/api/books', methods=['GET'])
def get_book_rating():
    book_name = request.args.get('name')
    print(book_name)
    book_parser = BookParser(book_name)
    book_parser.parse_pages()
    rating = book_parser.get_ratings()
    if rating:
        return jsonify({'name': book_name, 'rating': rating})
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
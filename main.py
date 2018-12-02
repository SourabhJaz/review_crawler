from book_parser import BookParser

if __name__ == "__main__":
    book_parser = BookParser("deep+work")
    book_parser.parse_pages()
    book_parser.get_ratings()

from parser import Parser
import re

class BookParser(Parser):
    pages = []

    def __init__(self, name):
        entity_name = self.parse_entity_name(name)
        urls = ["https://www.goodreads.com/search?query={}".format(entity_name)]
        self.urls = urls
        self.entity_name = entity_name
        
    def get_ratings(self):
        ratings = []
        for page in self.pages:
            try:
                ratingSpan = self.get_element(page, 'span', 'minirating')
                spanText = ratingSpan.text.strip()
                ratingText = spanText.split(" ")
                rating = float(ratingText[0])
                ratings.append(rating)
            except Exception:
                print("Couldn't find rating for the book")
                ratings = []
#            print("Ratings: {}".format(ratings))
            return ratings

    def get_result_names(self):
        names = []
        for page in self.pages:
            try:
                nameSpan = self.get_element(page, 'a', 'bookTitle')
                spanText = nameSpan.text.strip()
                names.append(spanText)
            except Exception:
                print("Couldn't find the book")
#            print("Names: {}".format(names))
            return names

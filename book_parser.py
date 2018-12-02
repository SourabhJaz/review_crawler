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
        rating = 0; count = 1; avg_rating = 0
        for page in self.pages:
            try:
                ratingSpan = self.get_element(page, 'span', 'minirating')
                spanText = ratingSpan.text.strip()
                ratingText = spanText.split(" ")
                rating += float(ratingText[0])
                avg_rating = (rating)/(count)
                count += 1
            except Exception:
                print("Couldn't find rating for the book")
            print("Rating: {}".format(avg_rating))

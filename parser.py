import requests
from bs4 import BeautifulSoup

class Parser():
    pages = []; entity_name = None; urls = []

    def parse_entity_name(self, name):
        return name

    def parse_pages(self):
        if len(self.pages) > 0:
            return
        urls = self.urls
        pageResponse = [requests.get(url) for url in urls]
        pages = [BeautifulSoup(page.text, 'html.parser') for page in pageResponse]
        self.pages = pages

    def get_element(self, page, type, name):
        element = page.find(type,class_=name)
        return element

    def print_pages(self):
        for page in self.pages:
            print(page.text)

    def get_urls(self):
        return [self.entity_name]

    def get_reviews(self):
        return []

    def get_ratings(self):
        return []
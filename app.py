import json

import requests
from bs4 import BeautifulSoup

from parsing.parser import Parsers


page = requests.get('https://blog.teclado.com/tag/web-development/').text


class App:
    def __init__(self, req_page):
        self.soup = BeautifulSoup(req_page, 'html.parser')

    def write_to_json(self):
        blog_list = []

        for article in self.soup.find_all('article'):
            locate = Parsers(article)
            headline = locate.headline
            sum_ary = locate.summary
            posts = locate.post_links

            blog_dict = {
                'Headline': headline,
                'Summary': sum_ary,
                'Post Link': posts
            }

            blog_list.append(blog_dict)

            with open('file_store.json', 'w') as file:
                json.dump(blog_list, file, indent=2)


obj = App(page)
obj.write_to_json()


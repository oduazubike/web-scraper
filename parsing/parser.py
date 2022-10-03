class Parsers:
    """Concerned with parsing the html tags and returns
    the values of the individual tags.

     Initialises `parent` as argument, `parent` is the
     individual `article` we iterate over"""

    def __init__(self, parent):
        self.parent = parent

    @property
    def headline(self):
        locator = self.parent.find('h2', class_='post-card-title').text
        return locator

    @property
    def summary(self):
        locator = self.parent.p.text
        return locator

    @property
    def post_links(self):
        locator = self.parent.find('a', class_='post-card-content-link')['href']
        post_link = f'https://blog.teclado.com{locator}'
        return post_link


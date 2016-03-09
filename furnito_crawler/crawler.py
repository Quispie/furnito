from __init__ import *

class Crawler:
    def __init__(self):
        self.base_url = config.base_url

    def get_categories(self):
        '''
        @usage: get categories of furnitures
        @return: categories of furnitures
        '''
        try:
            html = urlopen(self.base_url)
        except HTTPError as e:
            log.error_log("base_url unreachable")
        
        print self.base_url

crawler = Crawler()
crawler.get_categories()


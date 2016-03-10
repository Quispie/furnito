from __init__ import *

class URL_Manager:
    def __init__(self):
        self.base_url = config.base_url
        self.depth = config.depth

    def url_add(self):
        '''
        @usage: discover furniture url and push into url pool
        '''
        pass

    def url_remove(self, url):
        '''
        @usage: remove url that data has been crawled
        @arg: url, str, current url that has finished crawl
        '''
        pass

    def url_history(self, url):
        '''
        @usage: store history url that has been removed from url_pool, call this function after url_remove, store in log/url.txt
        @arg: url, str, removed url
        '''
        pass
        

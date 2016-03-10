import config

class URL_Manager:
    def __init__(self):
        self.base_url = config.base_url
        self.depth = config.depth

    def url_discover(self):
        '''
        @usage: discover furniture url and push into url pool
        @
        '''

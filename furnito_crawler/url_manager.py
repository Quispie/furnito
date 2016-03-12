class URL_Manager:
    def __init__(self):
        #url finished crawl
        self.visted = []
        #url need to crawl
        self.processing = []
    
    def get_visted(self):
        '''
        @usage: get url that has been crawled
        return list of url has been crawled
        '''
        return self.visted

    def get_processing(self):
        '''
        @usage: get url that need to be crawled
        @return list of url need to crawl
        '''
        return self.processing

    def url_add(self, url_list):
        '''
        @usage: discover furniture url and push into url pool
        @arg: list of url discovered from one furniture page
        '''
        #remove dulpilicate urls that not appear in both current list and history list
        diff = set(self.url_processing).difference(url_list)
        diff = set(self.url_visted).difference(diff)
        self.url_processing.extend(diff)

    def url_remove(self, url):
        '''
        @usage: remove url that data has been crawled, call before url_history
        @arg: url, str, current url that has finished crawl
        '''
        self.url_procsssing.remove(url)

    def url_history(self, url):
        '''
        @usage: store history url that has been removed from url_pool, call this function after url_remove
        @arg: url, str, removed url
        '''
        self.url_visted.append(url)
        

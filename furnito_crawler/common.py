class Common:
    def __init__(self):
        pass
    
    def remove_enter(self, url):
        '''
        @usage: remote all /n in url path
        @arg: plug in an url path
        @return: return cleaned url
        '''
        return url.strip()       

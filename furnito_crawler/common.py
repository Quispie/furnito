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

    def clean_feature(self, feature_list):
        '''
        @usage: clean feature list, remove all spaces
        @return furniture feature list
        ''' 
        feature_list = [x.strip(' ').replace(" ", "").replace("\n","") for x in feature_list]
        return feature_list

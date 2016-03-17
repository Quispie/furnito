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
        @arg: list of feature
        @return: furniture feature list
        ''' 
        feature_list = [x.strip(' ').replace("\n","") for x in feature_list]
        feature_list = [' '.join(x.split()) for x in feature_list]
        return feature_list

    def clean_reviews(self, review_list):
        '''
        @usage: clean review list, remove all spaces
        @arg: list of reviews
        @return: cleaned review list
        '''
        review_list = [x.strip(' ').replace("\n","") for x in review_list]
        review_list = [' '.join(x.split()) for x in review_list]
        return review_list

    def clean_filename(self, filename):
        '''
        @usage: modify filename, make sure there is no invaild symbol
        @arg: a filename
        @return: filename with no invalid symbol
        '''
        clean_filename = filename.replace(' ','_').translate(None, '/!@#$*\\')
        return clean_filename

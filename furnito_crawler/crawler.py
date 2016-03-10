from __init__ import *

class Crawler:
    def __init__(self):
        self.base_url = config.base_url

    def get_categories(self):
        '''
        @usage: get categories of furnitures
        @return: categories of furnitures
        '''
        #init category
        categories = {}

        try:
            html = urlopen(self.base_url)
        except HTTPError as e:
            log.error_log("base_url unreachable")
        #load page into bs_obj
        bs_obj = bs(html.read(), "lxml")
        #find categories
        try:
            nested_lists = bs_obj.findAll("i",{"class": re.compile("expand-open-close.*")})
        except AttributeError as e:
            log.error_log("can not find top level categories")
        if len(nested_lists) > 0:
            for nested_list in nested_lists: 
                category = nested_list.find_next("a")
                categories[category.text] = com.remove_enter(category['href'])
    
        return categories
            





                

crawler = Crawler()
crawler.get_categories()


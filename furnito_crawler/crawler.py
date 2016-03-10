from __init__ import *

class Crawler:
    def __init__(self, depth):
        self.base_url = config.base_url
        self.furnitures = []

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
            

    def get_furniture(self, url):
        '''
        @usage: get data from one furniture base on given url
        @arg: url or current furniture`
        '''
        furniture_page = requests.get(url)
        tree = html.fromstring(furniture_page.text)
        #extract tags
        name = tree.xpath('//span[@itemprop="name"]/h1/text()')[0]
        price = tree.xpath('//span[@itemprop="price"]/text()')[0]
        description = tree.xpath('//span[@itemprop="description"]/text()')[0]
        description_points = tree.xpath('//span[@itemprop="description"]/ul/li/text()')
        #as description points is a list, split list and add to description_main
        temp_str = ''
        for description_point in description_points:
            temp_str += description_point
        #add temp to description
        description += temp_str
        temp_str = ''
        #extract features
        features = tree.xpath('//tbody/tr/td/text()')
        features = com.clean_feature(features)
        for feature in features:
            temp_str += feature
        description += temp_str
         
        return [name, price, description]

    def get reviews(self, url):
                

crawler = Crawler(0)
test_url = "http://www.overstock.com/Home-Garden/TRIBECCA-HOME-Uptown-Modern-Sofa/3911915/product.html?refccid=L5DPRMJPPRDYV42KNMXUXX4GZE&searchidx=0"
print crawler.get_furniture(test_url)



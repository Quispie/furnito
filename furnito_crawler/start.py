from url_pool import URL_Pool
from url_manager import URL_Manager
from crawler import Crawler
import config

#init
processed = []
processing = []
um = URL_Manager(processed, processing)
crawler = Crawler()
#add start url into um
processing = um.url_add(config.base_url)
print processing
new_urls, crawled_url = crawler.get_result(config.base_url)

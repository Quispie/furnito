from url_pool import URL_Pool
from crawler import Crawler
import leveldb
 

up = URL_Pool()
crawler = Crawler()

alive_urls = up.get_alive_urls()
#start crawl
for alive_url in alive_urls:
    crawler.get_result(alive_url)

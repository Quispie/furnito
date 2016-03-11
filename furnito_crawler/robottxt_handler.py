import requests

class Robottxt_Handler:
    def __init__(self):
        self.url = 'http://www.overstock.com/robots.txt'
        self.base_url = 'http://www.overstock.com'

    def get_disallow_list(self):
        '''
        @usage: get access robot.txt, get disallow page list
        @return: disallow url list, remove from url_pool
        '''
        blocked_url = []
        robots_page = requests.get(self.url)
        robots_txt = robots_page.text
        lines = robots_txt.splitlines()
        for line in lines:
            if line.startswith("Disallow"):
                line = line.replace("Disallow: ","")
                if line.startswith("http"):
                    blocked_url.append(line)
                else:
                    blocked_url.append(self.base_url + line)
        return blocked_url

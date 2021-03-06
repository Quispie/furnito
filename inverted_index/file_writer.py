import config
import json

class File_Writer:
    def __init__(self):
        self.temp_path = config.temp_path
        self.pl_path = config.posting_list_path

    def write_temp(self, content):
        '''
        @usage: write content to a temprol storage
        @arg content: content need to write in temp
        '''
        with open(self.temp_path, 'a') as temp:
            temp.write(content)

    def write_posting_list(self, content):
        '''
        @usage: write posting list to local storage
        @arg content: content need to write
        '''
        with open(self.pl_path, 'w') as pl:        
            json.dump(content, pl)

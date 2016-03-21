import config
from os import listdir
from os.path import isfile, join
import json

#read file in the document, next step is to tokenize
class File_Reader:
    def __init__(self):
        self.path = config.file_path
        self.temp = config.temp_path
        self.pl_path = config.posting_list_path

    def load_file_names(self):
        '''
        @usage: load all furniture files into list
        @return: list of file names
        '''
        #load all file names from file path
        file_names = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        return file_names

    def read_file(self, file_name):
        '''
        @usage: read file content from current file
        @arg file_name: name of current file need to read
        @return content of current file
        '''
        with open(self.path+file_name, 'r') as f:
            return f.read().replace('\n', '')

    def read_temp(self):
        '''
        @usage: read temp file to get dictionary of inverted index
        @return: list of dictionary
        '''
        with open(self.temp, 'r') as f:
            return [tuple(map(str, x.split(','))) for x in f]

    def read_posting_list(self):
        '''
        @usage: read posting list
        @return: content of posting list
        '''
        with open(self.pl_path, 'r') as f:
           pl = json.load(f)
        return pl

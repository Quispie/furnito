from file_reader import File_Reader
from file_writer import File_Writer
import string
import config
import ast
from collections import OrderedDict, defaultdict
import pandas as pd
import numpy as np

class Invert_Index:
    def __init__(self):
        self.fr = File_Reader()
        self.fw = File_Writer()
        self.temp = config.temp_path
        self.csv_path = config.posting_list_path
        self.doc_num = 0
        self.term_num = 0
        self.term_list = []
    
    def build_dictionary(self):
        '''
        @usage: build dictionary of invert index, store in memory
        '''
        files = self.fr.load_file_names()
        for current_file in files:
            content = self.fr.read_file(current_file)
            content = self.clean(content)
            for term in content.split():
                self.term_list.append(term)
        #remove duplicate terms
        self.term_list = list(set(self.term_list))
        #sort alphabetly
        self.term_list = sorted(self.term_list)
        #store term num and doc number for build big-table store posting list
        self.doc_num = len(files)
        self.term_num = len(self.term_list)
        #add index to term list, store in hash table
        hash_dict = {}
        integer = 0
        for term in self.term_list:
            hash_dict[integer] = term
            integer += 1
        return hash_dict
    
    def build_posting_list(self):
        '''
        @usage: build posting list of inverted index, store in csv
        '''
        #init a data frame, rows are doc1, doc2..docn, columns are term1 term2...term m
        files = self.fr.load_file_names()
        df = pd.DataFrame(index = files, columns = self.term_list)
        df = df.fillna(0)
        for current_file in files:
            content = self.fr.read_file(current_file)
            content = self.clean(content)
            for term in content.split():
                #set current to 1
                df.xs(current_file, copy = False)[term] = 1
        df.to_csv(self.csv_path, sep = '\t', cols = self.term_list)
         

    def clean(self, content):
        '''
        @usage: clean current file, remove digit, punctuation, multiple space
        @arg content: argument content
        @return: cleaned content
        '''
        punc = set(string.punctuation)
        content = ''.join([x for x in content if not x.isdigit()])
        content = ''.join([x for x in content if x not in punc])
        content = ''.join([x.lower() for x in content])
        content = ' '.join(content.split())

        return content
            
ii = Invert_Index()
ii.build_dictionary()
ii.build_posting_list()

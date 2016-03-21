from invert_index import Invert_Index
import config
import json
from pprint import pprint

class VSM:
    def __init__(self):
        self.ii = Invert_Index()
        self.pl_path = config.posting_list_path
        self.pl = {}
        self.hash_dict = self.ii.posting_list()

    def get_termid(self, query_list):
        '''
        @usage: according user query, find term id from dictionary
        @arg query_list: list of user query
        @return: list of term id, example user query for [chair, desk], return [24, 45]
        '''
        #step 1, find index of current user query
        term_id = []
        for query in query_list:
            try:
                term_id.append(self.hash_dict.keys()[self.hash_dict.values().index(query)])
            except:
                pass
        return term_id

    def get_docs(self, term_id):
        '''
        @usage: according to query index, get related documents
        @arg: term_id, id of user query terms
        @return: dict of document location, {24: [doc1, doc5, doc7], 45: [doc8, dic11, doc22]}
        '''
        with open(self.pl_path) as pl_file:
            self.pl = json.load(pl_file)
        term_location = {}
        for term in term_id:
            term_location[term] = self.pl[str(term)]
        return term_location

    def build_vector_space(self, term_location):
        '''
        @usage: build table of vector space
        @arg term_location: userquery and it's location files
        @return: pandas data frame
        '''



vsm = VSM()
term_id = vsm.get_termid(['desk'])
get_docs = vsm.get_docs(term_id)

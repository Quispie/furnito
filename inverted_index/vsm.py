from invert_index import Invert_Index
import csv
import pandas as pd
import numpy as np
import config

class Vector_Space:
    def __init__(self):
        self.ii = Invert_Index()
        self.dicts, self.term_length = self.ii.build_dictionary()
        self.pl_path = config.posting_list_path

    def simple_vector_space(self, query_list):
        '''
        @usage: compute simple vector space value
        @arg query_list: list of user query
        @return: score
        '''
        #enlarge user query to a vector, first init a 1 by n matrix fill with 0
        query_vector = pd.DataFrame(index = [1], columns = range(0, self.term_length))
        query_vector = query_vector.fillna(0)
        #init term_id list, store index of user query
        term_id_list = []
        #loop through user query, map each query to it's id(from dictionary) and fill in df
        for query in query_list:
            try:
                term_id = self.dicts.keys()[self.dicts.values().index(query)]
                query_vector.xs(1, copy = False)[term_id] = 1
                term_id_list.append(term_id)
            except:
                pass
        #dot-product with relevant in the posting list store in dict : {doc: score}
        score_dict = {}
        query_vector = np.array(map(list, query_vector.values))
        print query_vector
        for df in pd.read_csv(self.pl_path, sep = ',', header = None, skiprows = 1, chunksize = 1):
            doc_vector = df.ix[:, df.columns != 0]
            #transform doc_vector and query_vector to list
            doc_vector = np.array(map(list, doc_vector.values))
            #print query_vector
            score = np.sum(query_vector * doc_vector)
            score_dict[df.iloc[0][0]] = score
            print score_dict

vs = Vector_Space()
vs.simple_vector_space(['a'])

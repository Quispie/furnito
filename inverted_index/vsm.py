from invert_index import Invert_Index
import csv
import pandas as pd
import numpy as np
import config

class Vector_Space:
    def __init__(self):
        self.ii = Invert_Index()
        self.dicts, self.term_length, self.doc_num = self.ii.build_dictionary()
        self.pl_path = config.posting_list_path

    def build_query_vector(self, query_list):
        '''
        @usage: according to user query build a query list
        @arg query_list: list of user query
        return: query vector
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
        
	query_vector = np.array(map(list, query_vector.values))
	return query_vector

    def simple_vector_space(self, query_vector):
        '''
        @usage: compute simple vector space value
        @arg query_list: list of user query
        @return: score
        '''
        #dot-product with relevant in the posting list store in dict : {doc: score}
        score_dict = {}
        for df in pd.read_csv(self.pl_path, sep = ',', header = None, skiprows = 2, chunksize = 1):
            doc_vector = df.ix[:, df.columns != 0]
            #transform doc_vector and query_vector to list
            doc_vector = np.array(map(list, doc_vector.values))
            #print query_vector
            score = np.sum(query_vector * doc_vector)
            score_dict[df.iloc[0][0]] = score
        print score_dict

    def tfidf_vector_space(self, query_vector):
        '''
        @usage: add tf-idf to simple vector space
        @arg query_list: list of user query
        @return: score
        '''
        score_dict = {}
        document_frequency = []
        doc_vector = []
        idf = None
        #read df, after skip 1row, the first row should be document frequency, other rows is term frequency
        is_document_frequency = True
        for df in pd.read_csv(self.pl_path, sep = ',', header = None, skiprows = 1, chunksize = 1):
            if is_document_frequency:
                document_frequency = df.ix[:,df.columns != 0]
                document_frequency = np.array(map(list, document_frequency.values))
                #compute idf term
                idf = self.idf(document_frequency)
                is_document_frequency = False
            else:
                doc_vector = df.ix[:, df.columns != 0]
                doc_vector = np.array(map(list, doc_vector.values))
                #first use doc_vector element-wise multiply idf
                doc_vector = doc_vector * idf
                score = np.sum(query_vector * doc_vector)
                score_dict[df.iloc[0][0]] = score
        print score_dict

    def idf(self, document_frequency):
        '''
        @usage: compute inverse document frequency
        @arg document_frequency: frequency of document
        @return score of idf
        '''
        idf = np.log2(float(self.doc_num + 1)/document_frequency)
        return idf

vs = Vector_Space()
query_vector = vs.build_query_vector(['a', 'chair'])
vs.tfidf_vector_space(query_vector)

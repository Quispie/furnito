import string
from invert_index import Invert_Index
import config
import json
import numpy as np
import pandas as pd
from file_reader import File_Reader
from file_writer import File_Writer

class VSM:
    def __init__(self):
        self.ii = Invert_Index()
        self.fr = File_Reader()
        self.fw = File_Writer()
        self.pl_path = config.posting_list_path
        self.pl = {}
        self.hash_dict = self.ii.posting_list()
        self.csv_path = config.vector_space_path

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

    def build_query_vector(self, term_id):
        '''
        @usage: build query vector
        @arg term_id: list of terms id
        @return: pandas data frame 1 row * n columns
        '''
        #build query vector
        #init a pandas data frame
        query_vector = pd.DataFrame(index = [1], columns = range(0, len(self.hash_dict)))
        query_vector = query_vector.fillna(0)
        for term in term_id:
            query_vector.xs(1, copy = False)[term_id] = 1
        query_vector = np.array(map(list, query_vector.values))
        return query_vector
    def build_vector_space(self, term_location, term_id):
        '''
        @usage: build simple vector space model
        @arg term_location: dict of term id and term docs, for example {1: [doc1, doc3]}
        @arg term_id: list of term id
        '''
        docs = self.fr.load_file_names()
        #init a dataframe, rows are docs, columns are terms
        df = pd.DataFrame(index = docs, columns = range(0, len(self.hash_dict)))
        df = df.fillna(0)
        #init a dictionary to store doc length
        doc_len = {}
        for current_doc in docs:
            content = self.fr.read_file(current_doc)
            content = self.clean(content)
            #add into doc_len dict, for furture normalize
            doc_len[current_doc] = len(content.split())
            for term in content.split():
                #get term_id by term
                term_id = self.hash_dict.keys()[self.hash_dict.values().index(term)]
                #add current dataframe
                df.xs(current_doc, copy = False)[term_id] += 1
        #insert a line into matrix indicate document frequency
        document_frequency = []
        for i in range(0, len(self.hash_dict)):
            #if current term >=1 means current term appear in doc
            temp_df = list(df.ix[:,i] >= 1)
            document_frequency.append(sum(temp_df))
        #write to dataframe
        df = pd.DataFrame(np.array([document_frequency]), columns = range(0, len(self.hash_dict))).append(df)
        df.to_csv(self.csv_path, sep = ',')
        return doc_len

    def simple_vector_space(self, query_vector):
        '''
        @usage: compute score of ranking use simple vector space
        @arg query_vector: vector of user query
        @return: dict of score
        '''
        score_dict = {}
        term_id = self.get_termid(query_vector)
        term_location = self.get_docs(term_id)
        query_vector = self.build_query_vector(term_id)

        unique_locations = []
        #get unique documents
        for k in term_location:
            unique_locations.extend(term_location[k])
        unique_locations = list(set(unique_locations))
        #get these lines from vector space
        for df in pd.read_csv(self.csv_path, sep = ',', header = None, skiprows = 2, chunksize = 1):
            current_row = df.ix[:,0].iloc[0]
            if current_row in unique_locations:
                #this row contains terms within user query
                doc_vector = df.ix[:, df.columns != 0]
                doc_vector = np.array(map(list, doc_vector.values))
                score = np.sum(query_vector * doc_vector)
                score_dict[df.iloc[0][0]] = score
        return score_dict


    def clean(self, content):
        '''
        @usage: clean content, remove
        @arg content: content of document
        @return: cleaned content
        '''
        punc = set(string.punctuation)
        content = ''.join([x for x in content if not x.isdigit()])
        content = ''.join([x for x in content if x not in punc])
        content = ''.join([x.lower() for x in content])
        content = ' '.join(content.split())

        return content







vsm = VSM()
vsm.simple_vector_space(['a', 'chair'])

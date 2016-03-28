from invert_index import Invert_Index
import config
import json
import string
from file_reader import File_Reader
import pandas as pd
import numpy as np

class PBM2:
    def __init__(self):
        self.ii = Invert_Index()
        self.hash_dict = self.ii.posting_list()
        self.pl_path = config.posting_list_path
        self.pl = {}
        self.fr = File_Reader()
        self.pbm_path = config.probability_space_path

    def get_termid(self, query_list):
        '''
        @usage: according to user query, find term id from dictionary
        @arg query_list: list of user query
        @return: list of term id
        '''
        term_id = []
        for query in query_list:
            try:
                term_id.append(self.hash_dict.keys()[self.hash_dict.values().index(query)])
            except:
                pass
        return term_id

    def get_docs(self, term_id):
        '''
        @usage: according to query index get related docs
        @arg: term_id, id of query terms
        @return dict of document location
        '''
        with open(self.pl_path) as pl_file:
            self.pl = json.load(pl_file)
        term_location = {}
        for term in term_id:
            term_location[term] = self.pl[str(term)]
        return term_location

    def build_probability_space(self):
        '''
        @usage: build probability space, including term frequency, document length
        '''
        docs = self.fr.load_file_names()
        #init data frame, store term id and docs
        df = pd.DataFrame(index = docs, columns = range(0, len(self.hash_dict)))
        df = df.fillna(0)
        #init dictionary to store document length
        doc_len = {}
        for current_doc in docs:
            content = self.fr.read_file(current_doc)
            content = self.clean(content)
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
        df.to_csv(self.pbm_path, sep = ',')
        return doc_len

    def simple_probability_model(self, query_vector):
        '''
        @usage: simple probability model
        @arg query_vector: list of user query
        @return: dict of score
        '''
        score_dict = {}
        term_id = self.get_termid(query_vector)
        term_location = self.get_docs(term_id)
        doc_length = self.build_probability_space()
        #add each term id by 1 equal to start index of probability space
        term_id = [x + 1 for x in term_id]
        unique_locations = []
        for k in term_location:
            unique_locations.extend(term_location[k])
        unique_locations = list(set(unique_locations))
        for df in pd.read_csv(self.pbm_path, sep = ',', header = None, encoding = 'utf-8', skiprows = 2, chunksize = 1):
            #compute probability of terms in current doc
            current_row = df.ix[:,0].iloc[0]
            if current_row in unique_locations:
                df1 = df.ix[:,term_id].copy()
                df1 = map(list, df1.values)[0]
                tf = reduce(lambda x, y: x*y, df1)
                score_dict[current_row] = float(tf)/doc_length[current_row]
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

    def idf(self, document_frequency):
        '''
        @usage: compute inverse document frequency
        @arg document_frequency: frequency of terms appear in document
        @return: score of idf
        '''
        idf = np.log2(float(len(self.fr.load_file_names()) + 1)/document_frequency)
        return idf


pbm = PBM2()
pbm.simple_probability_model(['chair', 'a'])

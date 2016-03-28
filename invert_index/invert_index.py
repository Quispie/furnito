from file_reader import File_Reader
from file_writer import File_Writer
import string
import config
from collections import OrderedDict, defaultdict

class Invert_Index:
    def __init__(self):
        self.fr = File_Reader()
        self.fw = File_Writer()
        self.temp = config.temp_path
        self.path = config.file_path

    def single_dictionary(self, file_name):
        '''
        @usage: load current document, clean, write to temprol file
        @arg file_name: current document name
        @return current single dictionary
        '''
        content = self.fr.read_file(file_name)
        content = self.clean(content)
        doc_length = 0
        #construct dict : docid
        f = open(self.temp, 'a')
        doc_length = len(content.split())
        for term in content.split():
            f.write(term + "," + file_name + "\n")
        f.close()
        return doc_length

    def multi_dictionary(self):
        '''
        @usage: generate full-dictionary, write doc length to json at the same time
        '''
        files = self.fr.load_file_names()
        doc_length_dict = {}
        for current_file in files:
            doc_length = self.single_dictionary(current_file)
            doc_length_dict[current_file] = doc_length
        self.fw.write_doc_length(doc_length_dict)


    def posting_list(self):
        '''
        @usage: construct inverted index, dictionary + posting list
        '''
        content = self.fr.read_temp()
        invert_index = defaultdict(list)
        for k, v in content:
            invert_index[k].append(v.strip())
        invert_index = dict(invert_index)
        #sort by key
        invert_index = OrderedDict(sorted(invert_index.items()))
        #seperate into dict + posting list
        #dict store term and term frequency
        #posting list store term and term position
        #extract all terms to a list to construct dic
        dicts = []
        hash_dict = {}
        [dicts.append(x) for x in invert_index]
        for value in range(0, len(dicts)):
            hash_dict[value] = dicts[value]
            invert_index[value] = invert_index.pop(dicts[value])
        self.fw.write_posting_list(invert_index)
        return hash_dict

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

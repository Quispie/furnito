import json
import config

class Json_Manager:
    def __init__(self):
        self.path = config.storage_path

    def json_writer(self, json_content, doc_name):
        '''
        @usage: export dict to json and store on local storage
        @arg: path, path to store json, string eg, 'downlaods/1.json'
        @arg: json_content, the content want to export, dictionary format
        '''
        with open(self.path + doc_name + ".json", 'w') as json_file:
            json.dump(json_content, json_file, ensure_ascii = True, indent = 2)

    def file_writer(self, content, doc_name):
        '''
        @usage: write furniture description into local storage
        @arg content: write content of furniture description
        '''        
        with open(self.path + doc_name, 'w') as f:
            f.write(content.encode('utf-8'))
        

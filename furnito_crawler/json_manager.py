import json

class Json_Manager:
    def __init__(self):
        pass

    def export_json(self, path, json_content):
        '''
        @usage: export dict to json and store on local storage
        @arg: path, path to store json, string eg, 'downlaods/1.json'
        @arg: json_content, the content want to export, dictionary format
        '''
        with open(path, 'w') as json_file:
            json.dump(json_content, json_file, ensure_ascii = True, indent = 2)
        

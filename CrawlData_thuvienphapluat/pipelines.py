import json
import json
import pymongo
from decouple import config
url = config('url')
client = pymongo.MongoClient(url)
db = client["sonnees"]

class JsonDBPipeline:
    def open_spider(self, spider):
        self.file = open('output.json', 'w', encoding='utf-8')
        self.file.write('[')
        self.first_item_written = False

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        if self.first_item_written:
            self.file.write(",\n"+line)
        else:
            self.file.write(line)
            self.first_item_written = True
        return item
    
    def close_spider(self, spider):
        if not self.first_item_written:
            self.file.truncate(0) # empty if not item
        else:
            self.file.write(']')
        self.file.close()


# class MongoDBPipeline:
#     def process_item(self, item, spider):
#         db.thuvienphapluat.insert_one(item)
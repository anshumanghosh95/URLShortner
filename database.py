# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.tinyurl
collection = db.url_details
counter = db.counter

class create_url():
    def __init__(self,url):
        self.url = url
        
    def tinyurl(self):
        old_record = collection.find_one({'url':self.url['url']})
        if old_record is None:
            count = counter.find_one()
            count = count['counter'] + 1
            counter.update_one({'counter': count - 1}, {'$set': {'counter': count}})
            self.url['_id'] = count
            self.url['tiny'] = 'http://localhost:5000/'+ str(count)
            url_tiny = str(self.url['tiny'])
            collection.insert_one(self.url)
        else:
            url_tiny = old_record['tiny']
        return url_tiny
    
class search_url():
    def __init__(self, keyword):
        self.keyword = keyword
    
    def search(self):
        pages = collection.find({'url': {'$regex':self.keyword}})
        pagedict = {}
        i = 1
        for page in pages:
            pagedict[i] = page['url']
            i += 1
        return pagedict
        
        
class page_url():
    def __init__(self, page_id):
        self.page_id = int(page_id)
    
    def page_name(self):
        page = collection.find_one({'_id':self.page_id})
        return (page['url'])
    
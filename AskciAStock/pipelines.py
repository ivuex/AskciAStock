# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from AskciAStock.utils.camel2underline import camel2underline

class AskciastockPipeline(object):

    def __init__(self, crawler):
        settings = crawler.settings.attributes
        print(settings.get('MONGODB_HOST').value, \
              settings.get('MONGODB_PORT').value, \
              settings.get('MONGODB_DB').value, \
              settings.get('MONGODB_USER').value, \
              settings.get('MONGODB_PWD').value, \
              settings.get('NAME').value,\
              '20202020=========')
        client = MongoClient(settings.get('MONGODB_HOST').value, settings.get('MONGODB_PORT').value)
        self.db = client[settings.get('MONGODB_DB').value]
        # self.db.authenticate(settings.get('MONGODB_USER').value, settings.get('MONGODB_PWD').value)
        self.collection_name = camel2underline(settings.get('NAME').value)
        print(self.collection_name, '-------')
        self.collection = self.db[self.collection_name]
        print(self.collection)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_item(self, item, spider):
        # raise(item)
        dictItem = dict(item)
        if not self.collection.find_one({'stock_code': dictItem['stock_code']}):
            self.collection.insert(dictItem)
        return item


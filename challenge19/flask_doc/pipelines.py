# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import redis
import json

class FlaskDocPipeline(object):
    def open_spider(self, spider):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)


    def process_item(self, item, spider):
        item['text'] = re.sub('\s+', ' ', item['text'])
#        print(url)
#        print(text)
        items = json.dumps(dict(item))
        self.redis.lpush('flask_doc:items', items)
        return item

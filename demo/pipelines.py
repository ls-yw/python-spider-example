# -*- coding: utf-8 -*-
import pymongo


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import demo.settings


class DemoPipeline(object):
    def __init__(self):
        host = demo.settings.mongodb_host
        port = demo.settings.mongodb_port
        dbname = demo.settings.mongodb_name
        table = demo.settings.mongodb_table
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[table]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

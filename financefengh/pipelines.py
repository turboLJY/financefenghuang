# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from store import collect_fengh_161212

class FinancefenghPipeline(object):
    def process_item(self, item, spider):
        if spider.name != "fenghnews" : return item
        if item.get("news_thread",None) is None: return item
        
        spec = {"news_thread": item["news_thread"]}
        collect_fengh_161212.fenghnews.update(spec,{'set':dict(item)},upsert=True)
        return None

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class TransitscraperPipeline(object):
    def process_item(self, item, spider):
        print 'processing %s' % item
        return item

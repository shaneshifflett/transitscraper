# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from transitmonitor.eta.models import ETA, DIRECTION_OPTS, Route, Vehicle, Stop
from django.db.utils import IntegrityError
from datetime import datetime

class ETAPipeline(object):
    def process_item(self, item, spider):
        return item

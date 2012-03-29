# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from transitmonitor.eta.models import ETA, DIRECTION_OPTS, Route, Vehicle, Stop
from django.db.utils import IntegrityError
from datetime import datetime

class ETAPipeline(object):
    def process_item(self, item, spider):
        print 'processing %s' % item
        name = item['trip_tag']
        direction = item['dir_tag']
        seconds = item['seconds']
        minutes = item['minutes']
        dept = item['is_departure']
        layover = item['affected_by_layover']
        routename = item['routename']
        stoptag = item['stoptag']
        vehicleid = item['vehicle_id']
        if layover == 'false':
            layover = False
        else:
            layover = True
        if dept == 'false':
            dept = False
        else:
            dept = True 
        if direction.find(DIRECTION_OPTS[0][0]) == -1 and direction.find(DIRECTION_OPTS[1][0]) == -1:
            direc = DIRECTION_OPTS[2][1]
        elif direction.find(DIRECTION_OPTS[0][0]) != -1:
            direc = DIRECTION_OPTS[0][1]
        else:
            direc = DIRECTION_OPTS[1][1]
        return item

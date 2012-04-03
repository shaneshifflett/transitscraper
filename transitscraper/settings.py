# Scrapy settings for transitscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import os
from time import time
from datetime import date


'''
sudo apt-get update
sudo apt-get install build-essential python2.7-dev python-pip libxml2-dev libxslt-dev git
sudo apt-get install binutils gdal-bin libproj-dev python-psycopg2
sudo apt-get install binutils gdal-bin libproj-dev postgresql-9.1-postgis postgresql-server-dev-9.1 python-psycopg2
scrapy crawl etascraper -o results/items-`date +"%d-%m-%Y-%s"`.csv -t csv

*/1 * * * * cd /home/ubuntu/transitscraper;/usr/local/bin/scrapy crawl etascraper -o /home/ubuntu/transitscraper/results/items-`date +"\%d-\%m-\%Y-\%s"`.csv -t csv 2>&1 >> /home/ubuntu/minute_script.log
*/3 * * * * cd /home/ubuntu/transitscraper;/usr/bin/python /home/ubuntu/transitscraper/sql_writer.py 2>&1 >> /home/ubuntu/three_minute_script.log
'''

BOT_NAME = 'transitscraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['transitscraper.spiders']
NEWSPIDER_MODULE = 'transitscraper.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'transitscraper.pipelines.ETAPipeline',
]

CONCURRENT_REQUESTS = 50

medate = str(date.fromtimestamp(time()))
LOG_FILE='%s-log.out' % medate
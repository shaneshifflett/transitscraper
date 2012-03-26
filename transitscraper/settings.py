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

BOT_NAME = 'transitscraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['transitscraper.spiders']
NEWSPIDER_MODULE = 'transitscraper.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

CONCURRENT_REQUESTS = 50

medate = str(date.fromtimestamp(time()))
#LOG_FILE='%s-log.out' % medate

def setup_django_env(path):
    import imp, os
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)       

    setup_environ(project)


current_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
setup_django_env(os.path.join(current_dir, '../transitmonitor/'))

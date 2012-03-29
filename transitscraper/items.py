# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class EtaScraperItem(Item):
    seconds = Field()
    minutes = Field()
    is_departure = Field()
    dir_tag = Field()
    vehicle_id = Field()
    trip_tag = Field()
    affected_by_layover = Field()
    routename = Field()
    stoptag = Field()
    created = Field()

from scrapy.spider import BaseSpider
from transitscraper.spiders.eta_urls import URL_LIST
from scrapy.selector import XmlXPathSelector
from transitscraper.items import EtaScraperItem

class EtaScraper(BaseSpider):
    name = "etascraper"
    allowed_domains = ["http://webservices.nextbus.com/"]
    end = int(len(URL_LIST)/2)
    start_urls = URL_LIST[1000:2000]

    def parse(self, response):
        xxs = XmlXPathSelector(response)
        routetitle = xxs.select('//predictions/@routeTitle').extract()[0]
        stoptag = xxs.select('//predictions/@stopTag').extract()[0]
        predictions = xxs.select('//prediction')
        items = []
        for prediction in predictions:
            item = EtaScraperItem()
            item['seconds'] = prediction.select('@seconds').extract()[0]
            item['minutes'] = prediction.select('@minutes').extract()[0]
            item['is_departure'] = prediction.select("@isDeparture").extract()[0]
            item['dir_tag'] = prediction.select('@dirTag').extract()[0]
            item['trip_tag'] = prediction.select('@tripTag').extract()[0]
            abl = prediction.select("@affectedByLayover").extract()
            if len(abl) > 0:
                item['affected_by_layover'] = abl
            else:
                item['affected_by_layover'] = 'false'
            items.append(item)
        return items
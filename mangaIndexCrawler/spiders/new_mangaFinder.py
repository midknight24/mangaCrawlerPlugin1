import scrapy
from .. import watchList

class newEpiSpider(scrapy.Spider):
    name = "newEpi"

    def start_requests(self):
        for url in watchList.wlist:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        #get result and check against db for newer epi
        result = response.css("#comiclistn dd:last-child a::attr(href)")[0].extract()
        #remove the page part
        result = result[:-5]
        result = "http://comic.kukudm.com"+result
        older = '0'#result from db
        if result != older:
            
            #update db

            yield {
                'url': result
            }

# -*- coding: utf-8 -*-
import scrapy


class DebtSpider(scrapy.Spider):
    name = 'debt'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['https://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//table[@class='datatableStyles__StyledTable-bwtkle-1 hOnuWY table table-striped']/tbody/tr") 

    
        for row in rows:
            counrty_name = row.xpath('.//td[1]/a[@href]/text()').get()
            debt = row.xpath(".//td[2]/text()").get()
            popluation = row.xpath(".//td[3]/text()").get()

            yield{
                "name: ": counrty_name, 
                "debt: ": debt, 
                "poplulation: ": popluation
            }



# -*- coding: utf-8 -*-

import scrapy
# from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request, Spider
from AskciAStock.items import AskciAStockItem
from AskciAStock.loaders import AskciAStockLoader
from scrapy_redis.spiders import RedisSpider
import re


class AskciAStockSpider(RedisSpider):
    name = 'askciAStock'
    allowed_domains = [
        's.askci.com'
    ]
    start_urls = [
        'http://s.askci.com/stock/a/',
    ]
    start_urls = start_urls + ['http://s.askci.com/stock/a/?reportTime=2018-06-30&pageNum=' + str(page) + '#QueryCondition' for page in list(range(2,178+1))]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        if re.search('&pageNum=\d+', response.url) or 'http://s.askci.com/stock/a/' == response.url:
            urls = response.xpath('//tbody//tr//td[2]/a/@href').extract()
            urls += response.xpath("//span[@class='pageBtnWrap']//a[@title='下一页']/@href").extract()
            for url in urls:
                yield Request('http://s.askci.com:80' + url, callback = self.parse_item)
        else:
            item = AskciAStockItem()
            item["stock_name"] = response.xpath("//div[@class='stock_details_tltie']//h1/text()").extract_first()
            item["stock_code"] = re.sub('[^\d]', '', response.xpath("//div[@class='stock_details_tltie']//h1/span/text()").extract_first())
            item["company_name"] = response.xpath("//tr[1]/td[2]/text()").extract_first()
            item["company_english_name"] = response.xpath("//tr[2]/td[2]/text()").extract_first()
            item["used_name"] = response.xpath("//tr[3]/td[2]/text()").extract_first()
            item["geographical_region"] = response.xpath("//tr[4]/td[2]/text()").extract_first()
            item["industry"] = response.xpath("//tr[5]/td[2]/text()").extract_first()
            item["company_website"] = response.xpath("//tr[6]/td[2]/text()").extract_first()
            item["primary_busines"] = response.xpath("//tr[7]/td[2]/text()").extract_first()
            item["product_name"] = response.xpath("//tr[8]/td[2]/text()").extract_first()
            item["controlling_shareholders"] = response.xpath("//tr[9]/td[2]/text()").extract_first()
            item["actual_controllers"] = response.xpath("//tr[10]/td[2]/text()").extract_first()
            item["ultimate_controller"] = response.xpath("//tr[11]/td[2]/text()").extract_first()
            item["chairman"] = response.xpath("//tr[12]/td[2]/text()").extract_first()
            item["managing_director_secretary"] = response.xpath("//tr[13]/td[2]/text()").extract_first()
            item["legal_representatives"] = response.xpath("//tr[14]/td[2]/text()").extract_first()
            item["general_manager"] = response.xpath("//tr[15]/td[2]/text()").extract_first()
            item["registered_capital"] = response.xpath("//tr[16]/td[2]/text()").extract_first()
            item["number_of_employees"] = response.xpath("//tr[17]/td[2]/text()").extract_first()
            item["phone_number"] = response.xpath("//tr[18]/td[2]/text()").extract_first()
            item["fax_number"] = response.xpath("//tr[19]/td[2]/text()").extract_first()
            item["post_code"] = response.xpath("//tr[20]/td[2]/text()").extract_first()
            item["office_address"] = response.xpath("//tr[21]/td[2]/text()").extract_first()
            item["company_profile"] = response.xpath("//tr[22]/td[2]/text()").extract_first()
            yield item

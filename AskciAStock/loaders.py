# -*- coding:utf-8 -*-

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class TakeLoader(ItemLoader):
    default_output_processor = TakeFirst()


class AskciAStockLoader(TakeLoader):
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())


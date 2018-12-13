# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field

class AskciAStockItem(Item):
    stock_name = Field()
    stock_code = Field()
    company_name = Field()
    company_english_name = Field()
    used_name = Field()
    geographical_region = Field()
    industry = Field()
    company_website = Field()
    primary_busines = Field()
    product_name = Field()
    controlling_shareholders = Field()
    actual_controllers = Field()
    ultimate_controller = Field()
    chairman = Field()
    managing_director_secretary = Field()
    legal_representatives = Field()
    general_manager = Field()
    registered_capital = Field()
    number_of_employees = Field()
    phone_number = Field()
    fax_number = Field()
    post_code = Field()
    office_address = Field()
    company_profile = Field()


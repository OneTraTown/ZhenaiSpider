# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ZhenaiwangItem(Item):
    photo_url = Field()
    nick_name = Field()
    member_id = Field()
    gender = Field()
    charm_value = Field()
    age = Field()
    height = Field()
    salary = Field()
    marital_status = Field()
    education = Field()
    work_place = Field()
    career = Field()
    sign = Field()
    mate_sele_standards = Field()
    native_place = Field()
    self_introdu = Field()
    hobbies = Field()
    home_page = Field()

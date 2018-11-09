# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    description=scrapy.Field()
    type=scrapy.Field()
    students=scrapy.Field()
class CangkuItem(scrapy.Item):
    id=scrapy.Field()
    name=scrapy.Field()
    update_time=scrapy.Field()
class ClassMessaageItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()

"""
爬取实验楼课程首页所有课程的名称、封面图片链接和课程作者。
课程名称和封面图片链接在课程主页就能爬到，
课程作者只有点击课程，进入课程详情页面才能看到，怎么办呢？
"""
class MultiPageItem(scrapy.Item):
    name=scrapy.Field()
    image=scrapy.Field()
    author=scrapy.Field()








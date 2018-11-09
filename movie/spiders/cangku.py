# -*- coding: utf-8 -*-
import scrapy

from movie.items import CangkuItem


class CangkuSpider(scrapy.Spider):
    name = 'cangku'
    allowed_domains = ['shiyanlou-courses']
    start_urls = ["https://github.com/shiyanlou?tab=repositories",
                   "https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoxOTo1NyswODowMM4FkpYw&tab=repositories"
                   ,"https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNVQxMTozMTowNyswODowMM4Bxrsx&tab=repositories",
                   "https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMFQxMzowMzo1MiswODowMM4BjkvL&tab=repositories",
                   ]

    def parse(self, response):
        for course in response.css('div#user-repositories-list li'):
            item=CangkuItem({
                'name': course.xpath('.//a/text()').extract_first().strip(),
                'update_time': course.xpath(".//relative-time/@datetime").extract_first()
            })
            yield item

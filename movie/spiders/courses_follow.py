# -*- coding: utf-8 -*-
import scrapy

from movie.items import ClassMessaageItem


class CoursesFollowSpider(scrapy.Spider):
    name = 'courses_follow'
    #allowed_domains = ['shiyanlou.com']
    start_urls = ['https://shiyanlou.com/courses/63']

    def parse(self, response):
        item=ClassMessaageItem(
            {
                'name': response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
              'author': response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
            }
        )
        yield item
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href'):
            yield response.follow(url,callback=self.parse)


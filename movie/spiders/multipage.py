# -*- coding: utf-8 -*-
import scrapy

from movie.items import MultiPageItem


class MultipageSpider(scrapy.Spider):
    name = 'multipage'
    allowed_domains = ['shiyanlou.com']
    #只是爬取首页的所有图片，课程名字，详情中的作者，所有url如下
    start_urls = ['https://www.shiyanlou.com/courses/']

    def parse(self, response):
        for ac  in response.css("a.course-box"):
            item=MultiPageItem(
                {
                  'name':ac.xpath('.//img/@alt').extract_first(),
                    'image':ac.xpath('.//img/@src').extract_first(),

                }
            )
            ## 构造课程详情页面的链接，爬取到的链接是相对链接，调用 urljoin 方法构造全链接
            course_url=response.urljoin(ac.xpath('@href').extract_first())
            # 构造到课程详情页的请求，指定回调函数
            reuest = scrapy.Request(course_url,callback=self.parse_aauthor)
            reuest.meta['item']=item
            yield reuest
    def parse_aauthor(self,response):
        #获取未完成的item
        item=response.meta['item']
        item['author']=response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        yield item




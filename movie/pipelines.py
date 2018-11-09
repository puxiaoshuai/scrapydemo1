# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 如果把 scrapy 想象成一个产品线，spider 负责从网页上爬取数据，Item 相当于一个包装盒，对爬取的数据进行标准化包装，然后把他们扔到Pipeline 流水线中。
#
# 主要在 Pipeline 对 Item
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from movie.models import Course, engin, Cangku,MyClass
from movie.items import CourseItem,CangkuItem,MultiPageItem,ClassMessaageItem
import  json
listdata=[]
class MoviePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,CourseItem):
            item['students']=int(item['students'])
            #self.session.add(Course(**item))
            data={'name':item['name'],'description':item['description'],'type':item['type'],'students':item['students']}
            listdata.append(data)
        elif isinstance(item,CangkuItem):
            datemsg=item['update_time']
            time=datetime.strptime(datemsg,"%Y-%m-%dT%H:%M:%SZ")
            item['update_time']=time
            self.session.add(Cangku(**item))#该session在open_spider中定义的
        elif isinstance(item,ClassMessaageItem):
            print(item['name'])
        elif isinstance(item,MultiPageItem):
            print(item['name'])
        return item

    def open_spider(self,spider):
        Session=sessionmaker(bind=engin)
        self.session=Session()
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
        if len(listdata)>0:
            with open('data.json','a',encoding='utf-8') as f:
                f.write(json.dumps(listdata))



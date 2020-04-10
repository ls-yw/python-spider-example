# -*- coding: utf-8 -*-
import scrapy
from demo.items import DemoItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口URL，扔到我们的调度器里
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']//li")
        for i in movie_list:
            douban_item = DemoItem()
            douban_item['serial_number'] = i.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i.xpath(
                ".//div[@class='info']//div[@class='hd']//a/span[1]/text()").extract_first()
            content = i.xpath(".//div[@class='item']//div[@class='bd']//p[1]/text()").extract()
            douban_item['introduce'] = ''
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduce'] = douban_item['introduce'] + content_s

            douban_item['star'] = i.xpath(
                ".//div[@class='bd']//div[@class='star']//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i.xpath(".//div[@class='bd']//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describe'] = i.xpath(".//div[@class='bd']//p[@class='quote']/span/text()").extract_first()
            yield douban_item
        next_link = response.xpath("//div[@class='paginator']/span[@class='next']/a/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('https://movie.douban.com/top250'+next_link, callback=self.parse)

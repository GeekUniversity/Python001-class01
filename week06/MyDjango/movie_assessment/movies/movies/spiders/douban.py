import scrapy
from scrapy.selector import Selector
from movies.items import  MoviesItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/1422283/']

    def start_requests(self):
        for i in range(20):
            url = f'https://movie.douban.com/subject/1422283/comments?start={i * 20}&limit=20&sort=new_score&status=P'
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # short_list = Selector(response=response).xpath('//*[@id="comments"]/div/div[2]/p/span/text()').getall()
        # star_list = Selector(response=response).xpath('//*[@id="comments"]/div/div[2]/h3/span[2]/span[2]//@class').getall()

        contexts = Selector(response=response).xpath('//*[@class="comment-item"]')
        for context in contexts:
            item = MoviesItem()
            item["short"] = context.xpath('.//*[@class="short"]/text()').extract_first()
            t_star = context.xpath('.//*[@class="comment-info"]/span[2]//@class').get()
            if t_star == 'allstar50 rating':
                item["n_star"] = 5
            elif t_star == 'allstar40 rating':
                item["n_star"] = 4
            elif t_star == 'allstar30 rating':
                item["n_star"] = 3
            elif t_star == 'allstar20 rating':
                item["n_star"] = 2
            elif t_star == 'allstar10 rating':
                item["n_star"] = 1
            else:
                item["n_star"] = 0
            yield item

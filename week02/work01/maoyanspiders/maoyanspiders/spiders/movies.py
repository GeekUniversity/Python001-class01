import scrapy
from scrapy.selector import Selector
from maoyanspiders.items import MaoyanspidersItem
class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        list01 = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl//dd/div[1]/a//@href').extract()
        for i in list01[0:10]:
            url = 'https://maoyan.com' + i
            yield scrapy.Request(url=url, callback=self.parse2)

    def parse2(self, response):
        item = MaoyanspidersItem()
        item['movie_name'] = Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()').extract()[0]
        list_type = Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()').extract()
        item['movie_type'] = ""
        for i in list_type:
            item['movie_type'] = item['movie_type'] + i + " "
        item['movie_time'] =  Selector(response=response).xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()').extract()[0]
        return  item



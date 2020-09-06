import scrapy
from scrapy.selector import Selector
from . import  db
from   spiders.items import  SpidersItem

class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    def start_requests(self):
        url = 'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/'
        yield scrapy.Request(url=url, callback=self.parse01)

    #获取前10的URL
    def parse01(self, response):
        for i in range(1,11):
            pro_url = Selector(response=response).xpath(f'//*[@id="feed-main-list"]/li[{i}]/div/div[2]/h5/a/@href').extract_first()
            yield scrapy.Request(url=pro_url, callback=self.parse02)

    #获取前10手机的产品名和产品描述，并写入数据库product_info
    def parse02(self, response):
        product_name  = Selector(response=response).xpath('//*[@id="feed-main"]/div[2]/div/div[1]/h1/text()').extract_first().strip()
        li = Selector(response=response).xpath('//*[@id="feed-main"]/div[3]/article/p/text()')
        worthy_num = Selector(response=response).xpath('//*[@id="rating_worthy_num"]/text()').extract_first().strip()
        unworthy_num =  Selector(response=response).xpath('////*[@id="rating_unworthy_num"]/text()').extract_first().strip()
        product_describe=''
        for i in li:
            text = i.get().strip()
            product_describe += text
        prod_id =  db.insert_production(product_name,product_describe,worthy_num,unworthy_num)
        current_url = response.request.url
        yield scrapy.Request(current_url, callback=self.parse03, dont_filter=True, meta={'prod_id':prod_id})

    #获取评论信息
    def parse03(self, response):
        item = SpidersItem()
        des_li = Selector(response=response).xpath('.//li[@class="comment_list"]/div[@class="comment_conBox"]/div[@class="comment_conWrap"]/div[@class="comment_con"]/p/span[@itemprop="description"]/text()')
        prod_id = response.meta['prod_id']
        item['product_id'] =  prod_id
        for i in des_li:
            item['assess_content'] = i.get().strip()
            if item['assess_content']:
                yield item
        next_url = Selector(response=response).xpath('.//li[@class="pagedown"]/a/@href').extract_first()
        if next_url != 'javascript:;' and  next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse03, meta={'prod_id':prod_id})














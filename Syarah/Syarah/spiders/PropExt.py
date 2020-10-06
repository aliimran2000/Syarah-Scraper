import scrapy


class PropextSpider(scrapy.Spider):
    name = 'PropExt'
    allowed_domains = ['syarah.com']
    start_urls = ['https://syarah.com/']


    def parse(self, response):
          response.xpath('//div[@class="container"]/div[@class="clearfix main_titles_box post_title"]/h1/span/text()')
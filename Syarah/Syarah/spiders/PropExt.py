import scrapy
import json


def containsdigit(stringval):
    for i in stringval:
        if i.isdigit():
            return True
    
    return False



class PropextSpider(scrapy.Spider):
    name = 'PropExt'
    allowed_domains = ['syarah.com']
    start_urls = ['https://syarah.com/']


    def __init__(self):
        with open('linksid.json') as f:
            data = json.load(f)        

        #for obj in data:
        self.start_urls.pop()

        for i in range(0,int(len(data)/100)):
            self.start_urls.append(data[i]['url'])



    def parse(self, response):
        title = response.xpath('//div[@class="container"]/div[@class="clearfix main_titles_box post_title"]/h1/span/text()').get()
        price = response.xpath('//div[@class="container"]/div[@class="clearfix main_titles_box post_title"]/span/i/text()').get()

        if containsdigit(price):
            yield {
                'title':title,
                'price':price
            }
        else:
            yield {
                'title':title,
                'price':None,
            }

$x('//div[@class="row post_ad_list_details"]/div[@class="col-lg-6 col-md-6 col-sm-12 col-xs-12"]/p/span/font/font')

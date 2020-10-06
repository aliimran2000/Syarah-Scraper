import scrapy





class LinksextractSpider(scrapy.Spider):
    name = 'LinksExtract'
    allowed_domains = ['syarah.com']
    start_urls = ['https://syarah.com/']

    def __init__(self):
        self.count = 0

        self.start_urls.pop()
        for i in range(1,665):
            str1 = 'https://syarah.com/?page='
            str2 = '&per-page=15'
            self.start_urls.append(str1+str(i)+str2)



    def parse(self, response):
        pass
        urlext = response.xpath('//div[@data-key]/ul/li/div/div/h2/a/@href').getall()

        for one in urlext:
            self.count += 1
            yield {
                'url' : one,
                'id' : self.count 
            }
    
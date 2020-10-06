import scrapy
import json


def containsdigit(stringval):
    for i in stringval:
        if i.isdigit():
            return True
    
    return False


def identifyfield(value):
    if ('الماركة' in value):
        return 'brand'

    if ('الموديل'in value):
        return 'model'

    if ('نوع الوقود'in value):
        return 'fueltype'
    
    if ('اللون'in value):
        return 'color'
    
    if ('الفئه'in value):
        return 'category'

    if ('الممشى'in value):
        return 'walkaway'

    if ('نوع القير'in value):
        return 'geartype'

    if ('المواصفات'in value):
        return 'specifications'

    if ('سعة المحرك' in value):
        return 'enginecapacity'
    
    if ('النوع' in value):
        return 'type'
    

    return value



#Type |النوع :

#model|الموديل :

#fueltpye |نوع الوقود :

#color |اللون:

#Category:|الفئه:

#price 





class PropextSpider(scrapy.Spider):
    name = 'PropExt'
    allowed_domains = ['syarah.com']
    start_urls = ['https://syarah.com/']


    def __init__(self):
        with open('linksid.json') as f:
            data = json.load(f)        

        #for obj in data:
        self.start_urls.pop()

        #for i in range(0,int(len(data)/100)):
        self.start_urls.append(data[7]['url'])



    def parse(self, response):
        title = response.xpath('//div[@class="container"]/div[@class="clearfix main_titles_box post_title"]/h1/span/text()').get()
        price = response.xpath('//div[@class="container"]/div[@class="clearfix main_titles_box post_title"]/span/i/text()').get()

        if (containsdigit(price)) == False:
            price = None

        data = response.xpath('//div[@class="row post_ad_list_details"]/div[@class="col-lg-6 col-md-6 col-sm-12 col-xs-12"]')
        Car={}
        Car['title'] = title
        Car['price'] = price


        for obj in data:
            key = obj.xpath('.//p/span[@class="title"]/text()').get()   
                    

            if ('fueltype' == identifyfield(key)):
                val = obj.xpath('.//p/span[@itemprop]/text()').get()
                Car['fueltype'] = val
                
            elif ('geartype' == identifyfield(key)):
                val = obj.xpath('.//p/span[@itemprop]/text()').get()
                Car['geartype'] = val
            
            elif ('specifications' == identifyfield(key)):
                val = obj.xpath('.//p/span[@itemprop]/text()').get()
                Car['specifications'] = val

            elif ('enginecapacity' == identifyfield(key)):
                val = obj.xpath('.//p/span[@itemprop]/text()').get()
                Car['enginecapacity'] = val

            elif ('walkaway' == identifyfield(key)):
                val = obj.xpath('.//p/span[not(@itemprop) and not(@class) ]/text()').get()
                Car['walkaway'] = val
            
            elif ('color' == identifyfield(key)):
                val = obj.xpath('.//p/span[@itemprop]/span[@class="circle-color"]/text()').get()
                Car['color'] = val

            elif ('model' == identifyfield(key)):
            val = obj.xpath('.//p/span[@itemprop]/span[@class="circle-color"]/text()').get()
            Car['color'] = val
            
    

        yield Car

            #if (identifyfield(all) == 'fueltype'):
            #    response.xpath('//div[@class="row post_ad_list_details"]/div[@class="col-lg-6 col-md-6 col-sm-12 col-xs-12"]/p/span[@class="title"]/text()').getall()


            

        #yield {
        #    'title':title,
        #    'price':price
        #}
      



#tital
#Brand |الماركة :  

#Type |النوع :

#model|الموديل :

#fueltpye |نوع الوقود :

#color |اللون:

#Category:|الفئه:

#price 

#walkawayt|الممشى:

#geartype|نوع القير :

#sepcifications |المواصفات:

#engine capacity |سعة المحرك:
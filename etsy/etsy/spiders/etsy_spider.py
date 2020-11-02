from scrapy import Spider
from scrapy import Request
from etsy.items import EtsyItem

class EtsySpider(Spider):
    name='etsy_spider'
    allowed_domains=['www.etsy.com']
    start_urls=['https://www.etsy.com/c/art-and-collectibles/prints/digital-prints?explicit=1&locationQuery=6252001&ref=pagination&page={}'.format(x) for x in range(1,251)]

    def parse(self, response):
        # product_urls = response.xpath('//ul[@class="responsive-listing-grid wt-grid wt-grid--block wt-justify-content-flex-start pl-xs-0"]/li/div/a/@href').extract()
        
        for i in range(1,65):
            xpath='//*[@id="content"]/div/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/div/ul/li[{}]/div/a/@href'.format(i)
            product_url = response.xpath(xpath).extract_first()
            yield Request(url=product_url, callback=self.parse_product_page)

    def parse_product_page(self, response):
        # Item will be yielded in this method

        # Company name
        name=response.xpath('//p[@class="wt-text-body-01 wt-mr-xs-1"]/a[@class="wt-text-link-no-underline"]/span/text()').extract()
        
        
        #product name
        prodname = response.xpath('//h1[@class="wt-text-body-03 wt-line-height-tight wt-break-word wt-mb-xs-1"]/text()').extract()
        
        
        # Product description
        description=''.join(response.xpath('//p[@class="wt-text-body-01 wt-break-word"]//text()').extract_first())
        
        # rating
        rating = response.xpath('//span[@class="wt-nudge-l-2"]/span/input/@value').extract_first()
        
        # savings
        amountsaved = response.xpath('//p[@class="wt-text-caption wt-text-slime"]/text()').extract_first()

        # price - review
        price = response.xpath('//div[@class="wt-display-flex-xs wt-align-items-center"]/p/text()').extract()
        

        #sales amount
        amountofsales = response.xpath('//p[@class="wt-text-body-03 wt-line-height-tight"]/text()').extract()
        
        #best seller
        bestseller =  response.xpath('//span[@class="wt-display-inline-block"]/text()').extract_first()
        

        #Initializing 
        item = EtsyItem()
        item['name'] = name
        item['prodname'] = prodname
        item['description'] = description
        item['rating'] = rating
        item['amountsaved'] = amountsaved
        item['price'] = price
        item['amountofsales'] = amountofsales
        item['bestseller'] = bestseller
        yield item


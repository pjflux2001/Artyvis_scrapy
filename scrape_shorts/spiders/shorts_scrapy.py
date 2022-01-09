import scrapy

class ShortsScrapySpider(scrapy.Spider):
    name = 'shorts_scrapy'
    allowed_domains = ['https://in.seamsfriendly.com/collections/shorts']
    start_urls = ['https://in.seamsfriendly.com/collections/shorts?page=1',
                'https://in.seamsfriendly.com/collections/shorts?page=2',
                'https://in.seamsfriendly.com/collections/shorts?page=3']
    
    def parse(self, response):
        print(response.url)
        for card in response.xpath("//div[@class='Grid__Cell 1/2--phone 1/2--tablet-and-up 1/3--desk']"):
            title = card.xpath(".//div//div//div//h2//a/text()").get()
            description = card.xpath(".//div//div//div[@class='label_icon label_icon-mob']/text()").get()
            price = card.xpath(".//div//div//div//div//span/text()").get()
            img_urls = []
            img_url = "https:" + card.xpath(".//div//div//a//div//img/@data-src").get()
            widths = card.xpath(".//div//div//a//div//img/@data-widths").get().replace("[","").replace("]","").split(',')
            for w in widths:
                img_urls.append(img_url.replace("{width}",w))
            print(title)
            print(description)
            print(price)
            print(img_urls)

            yield {
                'Title': title,
                'Description': description,
                'Price': price,
                'Image URLs': img_urls
            }
        pass

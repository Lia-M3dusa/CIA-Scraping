import scrapy


#links= //a[starts-with(@href, "colletion") and (parent::h3|h2)]/@href
#titulos= //div[@class="documentContent"]/h1/text()
#content = //div[@class="field-item even"]//p[not(@class)]/text()
#img = 

class SpiderCia(scrapy.Spider):

    name= 'cia'
    start_urls= [
        'https://www.cia.gov/readingroom/historical-collections']
    
    custom_settings = {
        'FEEDS': {
            'cia.json': {
                'format': 'json',
                'encoding': 'utf-8',
                'indent': 4,
            }
        },
    }

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath(
            '//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath(
            '//div[@class="field-item even"]//p[not(@class)]/text()').getall()
        img = response.xpath(
            '//div[@class="field-item even"]//a[not(@class) and @target="_blank"]/img/@src').get()

        yield {
            'url': link,
            'tittle': title,
            'paragraph': paragraph,
            'img': img
        }


    def parse(self, response):
        linkUnlock = response.xpath(
            '//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()
        for link in linkUnlock:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    
    
        

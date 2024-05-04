import scrapy

class QuoteSpider(scrapy.Spider):
    name='quote-spider'
    start_urls=['https://poshmark.com/category/Men']
    def parse(self, response):
        BOX_SELECTOR='.title__condition__container'
        TEXT_SELECTOR='.tile__title.tc--b::text'

        for box in response.css(BOX_SELECTOR):
            yield{
                'text':box.css(TEXT_SELECTOR).extract_first(),
            }
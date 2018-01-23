import scrapy


class KistaSpider(scrapy.Spider):
    name = "kista"

    def start_requests(self):
        urls = ['https://www.hemnet.se/bostader?location_ids%5B%5D=473377&item_types%5B%5D=bostadsratt',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'sold': response.css("span.result-type-toggle__sold-count::text").re(r'\d+'),
            'for_sell': response.css("span.result-type-toggle__for-sale-count::text").re(r'\d+')
        }
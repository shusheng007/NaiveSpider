import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://jinqiangua.911cha.com/',
    ]

    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield scrapy.Request(url,headers=headers)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'gua-%s' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
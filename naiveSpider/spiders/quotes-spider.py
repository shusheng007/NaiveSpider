import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://jinqiangua.911cha.com/111111.html',
        'https://jinqiangua.911cha.com/000000.html'
    ]

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'gua-%s' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('saved file %' % filename)
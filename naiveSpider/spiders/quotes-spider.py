import scrapy
import random


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'https://jinqiangua.911cha.com/',
    ]


     my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
     'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
     ]
	



    def start_requests(self):

        headers= {'User-Agent': random.choice(headers) }
        for url in self.start_urls:
            yield scrapy.Request(url,headers=headers)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'gua-%s' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
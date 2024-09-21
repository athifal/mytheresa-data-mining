import scrapy


class MytheresaSpiderSpider(scrapy.Spider):
    name = "mytheresa_spider"
    allowed_domains = ["mytheresa.com"]
    start_urls = ["https://mytheresa.com"]

    def parse(self, response):
        pass

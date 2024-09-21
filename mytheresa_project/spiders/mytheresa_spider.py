import scrapy

class MyTheresaSpider(scrapy.Spider):
    name = "mytheresa_spider"
    allowed_domains = ["mytheresa.com"]
    start_urls = ["https://www.mytheresa.com/int/en/men/shoes"]

    def parse(self, response):
        # Extract product URLs on the current page
        product_urls = response.css('a.item__link::attr(href)').getall()
        for url in product_urls:
            yield response.follow(url, self.parse_product)

        # Extract the "Show more" button URL
        show_more_url = response.css('div.loadmore__button a.button::attr(href)').get()
        if show_more_url:
            yield response.follow(show_more_url, self.parse)

    def parse_product(self, response):
         
        # Extract and yield product details
        breadcrumbs = response.css('div.breadcrumb__item a.breadcrumb__item__link::text').getall()
        product_name = response.css('a.product__area__branding__designer__link::text').get().strip()
        yield {
            'Sl. No': 1,
            'Field Name': 'breadcrumbs',
            'Field Type': 'list',
            'Example': breadcrumbs,
        }
        yield {
            'Sl. No': 2,
            'Field Name': 'product_name',
            'Field Type': 'string',
            'Example': product_name,
        }
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

        # Extract the total number of pages
        total_pages = response.css('a.button::attr(href)').re(r'page=(\d+)')
        if total_pages:
            max_pages = max(map(int, total_pages))  # Find the highest page number

            # Get the current page number
            current_page = int(response.url.split('page=')[-1]) if 'page=' in response.url else 1

            # Request the next page if within the total pages
            if current_page < max_pages:
                next_page = f"https://www.mytheresa.com/int/en/men/shoes?page={current_page + 1}"
                yield scrapy.Request(next_page, callback=self.parse)

    def parse_product(self, response):
        self.product_counter += 1  # Increment product counter for each product
        product_number = self.product_counter  # Store the current product number
        # Extract and yield product details
        breadcrumbs = response.css('div.breadcrumb__item a.breadcrumb__item__link::text').getall()
        product_name = response.css('a.product__area__branding__designer__link::text').get().strip()
        yield {
            'Product No': product_number,
            'Sl. No': 1,
            'Field Name': 'breadcrumbs',
            'Field Type': 'list',
            'Example': breadcrumbs,
        }
        yield {
            'Product No': product_number,
            'Sl. No': 2,
            'Field Name': 'product_name',
            'Field Type': 'string',
            'Example': product_name,
        }
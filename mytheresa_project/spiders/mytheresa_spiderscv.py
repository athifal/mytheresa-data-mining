import scrapy
import csv

class MyTheresaSpider(scrapy.Spider):
    name = "mytheresa_spiderscsv"
    allowed_domains = ["mytheresa.com"]
    start_urls = ["https://www.mytheresa.com/int/en/men/shoes"]

    def __init__(self):
        self.product_counter = 1
        self.output_file = 'products.csv'
        # Open the CSV file for writing
        self.csv_file = open(self.output_file, 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)
        # Write the header row
        self.csv_writer.writerow(['Sl. No', 'Field Name', 'Field Type', 'Example'])

    def parse(self, response):
        product_urls = response.css('a.item__link::attr(href)').getall()
        for url in product_urls:
            yield response.follow(url, self.parse_product)
              

        show_more_url = response.css('div.loadmore__button a.button::attr(href)').get()
        if show_more_url:
            yield response.follow(show_more_url, self.parse)
    def parse_product(self, response):
        # Extract product details
        description = response.css('div.accordion__body__content > p::text').get()
        description = description.strip() or None  # Extract only the item number
        product_data = {
            'breadcrumbs': response.css('div.breadcrumb__item a.breadcrumb__item__link::text').getall(),
            'product_image': response.css('img.product__gallery__carousel__image::attr(src)').get(default=None),
            'brand_name': response.css('a.product__area__branding__designer__link::text').get(default='').strip(),
            'product_name': response.css('div.product__area__branding__name::text').get(default='').strip(),
            'product_price': response.xpath('normalize-space(//span[contains(@class, "pricing__prices__value")])').get(default=None),
            'product_id': response.css('li::text').re_first(r'Item number: (\w+)'),
            'Description': description,
            'Sizes': response.css('div.sizeitem span.sizeitem__label::text').getall(),
            'other_images': response.css('div.swiper-slide img::attr(src)').getall()[1:7],
        }

        # Write product details to CSV
        for field_name, example in product_data.items(): 
            self.csv_writer.writerow([self.product_counter, field_name, 'list' if isinstance(example, list) else 'string', str(example)])
            self.product_counter += 1

    def close(self, reason):
        # Close the CSV file when done
        self.csv_file.close()

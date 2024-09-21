import scrapy

class MyTheresaSpider(scrapy.Spider):
    name = "mytheresa_spider"
    allowed_domains = ["mytheresa.com"]
    start_urls = ["https://www.mytheresa.com/int/en/men/shoes"]

    def __init__(self):
        self.product_counter = 1

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
        product_image = response.css('img.product__gallery__carousel__image::attr(src)').get()
        brand_name = response.css('a.product__area__branding__designer__link::text').get().strip()
        product_name = response.css('div.product__area__branding__name::text').get().strip()
        product_price = response.xpath('normalize-space(//span[contains(@class, "pricing__prices__value")])').get()
        item_number = response.css('li::text').re_first(r'Item number: (\w+)')  # Extract only the item number
        sizes = response.css('div.sizeitem span.sizeitem__label::text').getall()
        image_urls = response.css('div.swiper-slide img::attr(src)').getall()
        yield {
            'Sl. No': self.product_counter,
            'Field Name': 'breadcrumbs',
            'Field Type': 'list',
            'Example': str(breadcrumbs),
        }
        self.product_counter += 1
        yield {
             'Sl. No': self.product_counter,
             'Field Name': 'product_image',
             'Field Type': 'string',
             'Example': str(product_image),
        }
        self.product_counter += 1
        yield {
            'Sl. No':self.product_counter,
            'Field Name': 'brand_name',
            'Field Type': 'string',
            'Example': str(brand_name),
        }
        self.product_counter += 1
        yield {
            'Sl. No':self.product_counter,
            'Field Name': 'product_name',
            'Field Type': 'string',
            'Example': str(product_name),
        }
        self.product_counter += 1
        yield {
            'Sl. No':self.product_counter,
            'Field Name': 'product_price',
            'Field Type': 'string',
            'Example': str(product_price),
        }
        self.product_counter += 1
        yield {
            'Sl. No':self.product_counter,
            'Field Name': 'product_id',
            'Field Type': 'string',
            'Example': str(item_number),
        }
        self.product_counter += 1
        yield {
            'Sl. No':self.product_counter,
            'Field Name': 'Sizes',
            'Field Type': 'list',
            'Example': str(sizes),
        }
        self.product_counter += 1
        yield {
            'Sl. No':self.product_counter,
            'Field Name': 'other_images',
            'Field Type': 'list',
            'Example': str(image_urls[1:]),
        }
        self.product_counter += 1
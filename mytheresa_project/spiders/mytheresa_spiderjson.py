import scrapy

class MyTheresaSpider(scrapy.Spider):
    name = "mytheresa_spiderjson"
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
        product_image = response.css('img.product__gallery__carousel__image::attr(src)').get()
        brand_name = response.css('a.product__area__branding__designer__link::text').get()
        product_name = response.css('div.product__area__branding__name::text').get()
        product_price = response.xpath('normalize-space(//span[contains(@class, "pricing__prices__value--original")]/span[contains(@class, "pricing__prices__price")])').get()
        item_number = response.css('li::text').re_first(r'Item number: (\w+)')  # Extract only the item number
        sizes = response.css('div.sizeitem span.sizeitem__label::text').getall()
        description = response.css('div.accordion__body__content > p::text').get()
        description = description.strip() or None
        image_urls = response.css('div.swiper-slide img::attr(src)').getall()[1:7]

        product_data = {
            "breadcrumbs": breadcrumbs,
            "image_url": product_image,
            "brand": brand_name,
            "product_name": product_name,
            "listing_price": product_price,
            "offer_price": None,  # offer price info not available in website
            "discount": None,  #  discount info not available in website
            "product_id": item_number,
            "description": description,
            "sizes": sizes,
            "other_images": image_urls
        }

        # Yield the product data directly
        yield product_data

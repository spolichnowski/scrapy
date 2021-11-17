import scrapy


class SmartPhoneSpider(scrapy.Spider):
    name = "smartphones"

    start_urls = ["https://www.komputronik.pl/search-filter/1596/smartfony-z-dual-sim"]

    def parse(self, response):
        smartphone_page = response.css("div.pe2-head a")
        yield from response.follow_all(smartphone_page, self.parse_smartphone)

        pagination_links = response.xpath("//li[@class='pgn-static']//a/i/..")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_smartphone(self, response):
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        yield {
            "name": extract_with_css("section.p-inner-name h1::text"),
            "price": extract_with_css("span.price span.proper::text"),
            "processor": response.xpath(
                "//*[contains(text(), 'Zastosowany procesor')]/following::td/text()"
            )
            .get(default="")
            .strip(),
        }

import scrapy
from ..items import SmartphoneItem
from scrapy.loader import ItemLoader


class SmartPhoneSpider(scrapy.Spider):
    name = "smartphones"

    start_urls = ["https://www.komputronik.pl/search-filter/1596/smartfony-z-dual-sim"]

    def parse(self, response):
        smartphone_page = response.css("div.pe2-head a")
        yield from response.follow_all(smartphone_page, self.parse_smartphone)

        pagination_links = response.xpath("//li[@class='pgn-static']//a/i/..")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_smartphone(self, response):

        load = ItemLoader(item=SmartphoneItem(), response=response)
        load.add_css("smt_name", "section.p-inner-name h1::text"),
        load.add_css("price", "span.price span.proper::text"),
        load.add_xpath(
            "processor",
            "//*[@id='p-content-specification']/div[2]/div/div[5]/table/tbody/tr[1]/td",
        ),
        yield load.load_item()

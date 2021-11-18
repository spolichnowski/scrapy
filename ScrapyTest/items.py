# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from typing import Optional
import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from w3lib.html import remove_tags


def format_output(value):

    return value.strip().replace("\n", "").replace(u"\xa0", u" ")


class SmartphoneItem(scrapy.Item):
    smt_name = scrapy.Field(input_processor=MapCompose(remove_tags, format_output))
    price = scrapy.Field(input_processor=MapCompose(remove_tags, format_output))
    processor = scrapy.Field(input_processor=MapCompose(remove_tags, format_output))

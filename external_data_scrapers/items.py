import scrapy


class ParkingLocationItem(scrapy.Item):
    date = scrapy.Field()
    location = scrapy.Field()
    daily_available = scrapy.Field()
    daily_free = scrapy.Field()
    subscriber_available = scrapy.Field()
    subscriber_rented = scrapy.Field()
    subscriber_free = scrapy.Field()
    subscriber_waiting_list = scrapy.Field()

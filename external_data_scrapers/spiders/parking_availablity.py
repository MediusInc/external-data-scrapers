import scrapy
import time
from ..items import ParkingLocationItem

def conv(num: str) -> int:
    try:
        return int(num)
    except ValueError:
        return None

class ParkingSpider(scrapy.Spider):
    name = 'parking-availability'
    start_urls = ['https://www.lpt.si/parkirisca/informacije-za-parkiranje/prikaz-zasedenosti-parkirisc']

    def parse(self, response):
        places = response.xpath(
            "//main/div/div/div/div/table/tbody/tr").getall()

        t = time.time()
        place_item = ParkingLocationItem()
        for place_i in range(len(places)):
            place_item['date'] = int(t*1000)
            place_item['location'] = response.xpath(f"((//main/div/div/div/div/table/tbody/tr)[{place_i+1}]/td)[1]/a/text()").get()
            place_item['daily_available'] = conv(response.xpath(f"((//main/div/div/div/div/table/tbody/tr)[{place_i+1}]/td)[2]/div/p[2]/text()").get())
            place_item['daily_free'] = conv(response.xpath(f"((//main/div/div/div/div/table/tbody/tr)[{place_i+1}]/td)[2]/div/p[3]/text()").get())
            place_item['subscriber_available'] = conv(response.xpath(f"((//main/div/div/div/div/table/tbody/tr)[{place_i+1}]/td)[3]/div/p[1]/text()").get())
            place_item['subscriber_rented'] = conv(response.xpath(f"((//main/div/div/div/div/table/tbody/tr)[{place_i+1}]/td)[3]/div/p[2]/text()").get())
            place_item['subscriber_free'] = conv(response.xpath(f"((//main/div/div/div/div/table/tbody/tr)[{place_i+1}]/td)[3]/div/p[3]/text()").get())
            place_item['subscriber_waiting_list'] = conv(response.xpath(f"((//main/div/div/div/div/table/tbody/tr)[{place_i+1}]/td)[3]/div/p[4]/text()").get())

            yield place_item

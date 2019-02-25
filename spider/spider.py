from pathlib import Path
import time
from urllib.parse import urlparse

import scrapy


class Spider(scrapy.Spider):
    name = 'medicalxpress'
    start_urls = ['http://medicalxpress.com/sort/date/all/']

    def parse(self, response):
        num_yielded = 0
        for article in response.css('.news-link'):
            url = article.css('a::attr("href")').get('')
            path = urlparse(url).path
            path = Path(path).stem
            yield {'Path': path, 'Title': article.css('a::text').get()}
            num_yielded += 1
        if num_yielded == 0:
            # Pages with no articles were discovered toward the end, signaling the end.
            return

        next_page = response.css('li.page-item:nth-child(2) a::attr("href")').get()
        if next_page is not None:
            time.sleep(.5)
            yield response.follow(next_page, self.parse)

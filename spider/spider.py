from pathlib import Path
from urllib.parse import urlparse

import scrapy


class Spider(scrapy.Spider):
    name = 'medicalxpress'
    start_urls = ['https://medicalxpress.com/sort/date/all/']

    def parse(self, response):
        for article in response.css('.news-link'):
            url = article.css('a::attr("href")').get('')
            path = urlparse(url).path
            path = Path(path).stem
            yield {'Path': path, 'Title': article.css('a::text').get()}

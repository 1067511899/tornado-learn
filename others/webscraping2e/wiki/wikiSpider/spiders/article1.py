from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
import logging

fhand = logging.FileHandler('new.log', mode='a', encoding='GBK')
logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                    handlers=[fhand],
                    format=
                    '%(asctime)s  - %(levelname)s: %(message)s'
                    # 日志格式
                    )


class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['to8to.com']
    start_urls = ['http://sz.to8to.com/zwj/']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        url = response.url
        
        title = response.css('h1::text').extract_first()
        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        lastUpdated = lastUpdated.replace('This page was last edited on ', '')
        print('URL is: {}'.format(url))
        print('title is: {} '.format(title))
        print('text is: {}'.format(text))
        print('Last updated: {}'.format(lastUpdated))
        logging.info(url)
        logging.info(title)
        logging.info(text)
        logging.info(lastUpdated)

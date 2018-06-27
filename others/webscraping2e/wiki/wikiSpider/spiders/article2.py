import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'
    
    def start_requests(self):
        urls = [
            'http://sz.to8to.com/zwj/']
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]
    
    def parse(self, response):
        url = response.url
        title = response.xpath('//a')
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))
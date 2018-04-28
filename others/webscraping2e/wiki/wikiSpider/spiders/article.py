import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'
    
    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Python_(programming_language)']
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]
    
    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))
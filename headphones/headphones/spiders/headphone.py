import scrapy

class QuotesSpider(scrapy.Spider):
    name = "headphone"

    def start_requests(self):
        urls = [

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
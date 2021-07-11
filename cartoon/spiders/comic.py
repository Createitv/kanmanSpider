import scrapy
from scrapy.linkextractors import LinkExtractor
import json,os
import requests


class ComicSpider(scrapy.Spider):
    name = 'comic'
    # start_urls = [f'https://www.kanman.com/{URL_ID}']
    start_urls = []
    
    def __init__(self,urlId=None,*args,**kwargs):
        super(eval(self.__class__.__name__), self).__init__(*args, **kwargs)
        self.urlId = urlId
        self.start_urls = [f'https://www.kanman.com/{urlId}']

    def parse(self, response):
        links = LinkExtractor(restrict_css='#j_chapter_list li')
        links = links.extract_links(response)
        for link in links:
            yield scrapy.Request(url=link.url, callback=self.parse_item)

    def parse_item(self, response):
        uid = response.url.split('/')[-1].split('.')[0]
        api_url = f"https://www.kanman.com/api/getchapterinfov2?product_id=1&productname=kmh&platformname=pc&comic_id={self.urlId}&chapter_newid={uid}&isWebp=1&quality=middle"
        yield scrapy.Request(url=api_url, callback=self.parse_detail)

    def parse_detail(self, response):
        data = json.loads(response.text).get("data")
        # print(data)
        comic_name = data.get('comic_name')
        last_chapter_name = data.get('last_chapter_name')
        img_urls = data['current_chapter']['chapter_img_list']
        end_num = data['current_chapter']['end_num']
        chapter_name = data['current_chapter']['chapter_name']

        if not os.path.exists(f'./{comic_name}/{chapter_name}'):
            os.makedirs(f'./{comic_name}/{chapter_name}')

        for j, url in enumerate(img_urls, 1):
            with open(f'./{comic_name}/{chapter_name}/{j}.jpg', 'wb') as f:
                f.write(requests.get(url).content)

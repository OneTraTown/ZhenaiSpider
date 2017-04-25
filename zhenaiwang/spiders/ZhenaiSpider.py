from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from ..items import ZhenaiwangItem
import json
import traceback
from get_urls import get_starts_urls
import random
import requests
class ZhenaiSpider(RedisSpider):

    name = 'ZhenaiSpider'
    redis_key = 'ZhenaiSpider:urls'
    allowed_domains = ['zhenai.com']

    start_urls = get_starts_urls()
    ua_useragent = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"]
    user_agent = random.choice(ua_useragent)
    global user_agent

    def start_requests(self):
        headers = {'User-Agent': user_agent}
        for url in self.start_urls:
            yield Request(url=url, headers=headers, method='GET', callback=self.parse_list)

    #def start_requests(self):
    #    urls = get_starts_urls()
    #    for url in urls:
    #        yield Request(url = url, callback = self.parse_list)

    def parse_list(self, response):
        data = {}
        headers = {'User-Agent': user_agent}
        try:
            data = json.loads(response.text)
        except:
            traceback.print_exc()
        if data and 'data' in data:
            data_list = data['data']
            for item in data_list:
                member_id = item['memberId']
                url = 'http://album.zhenai.com/u/{}?flag=s'.format(member_id)
                yield Request(url = url, headers = headers, callback = self.parse_item)

    def parse_item(self, response):
        sel = Selector(response)
        item = ZhenaiwangItem()
        try:
            item['home_page'] = response.url
            pic_url = sel.xpath('//div[@id="AblumsThumbsListID"]/ul/li/p/img[1]/@data-big-img').extract()
            item['photo_url'] = pic_url

            item['nick_name'] = sel.xpath('//a[@class="name fs24"]/text()').extract_first()
            item['member_id'] = sel.xpath('//p[@class="brief-info fs14 lh32 c9f"]/text()').extract()[0][3:].strip()
            item['charm_value'] = sel.xpath('//p[@class="brief-info fs14 lh32 c9f"]/span[2]/span/text()').extract()[0].strip()

            brief_table = sel.xpath('//table[@class="brief-table"]//td/text()').extract()

            item['native_place'] = brief_table.pop()
            item['sign'] = brief_table.pop()
            item['career'] = brief_table.pop()
            item['work_place'] = brief_table.pop()
            item['education'] = brief_table.pop()
            item['marital_status'] = brief_table.pop()
            item['salary'] = brief_table.pop()
            item['height'] = brief_table.pop()
            item['age'] = brief_table.pop()

            item['self_introdu'] = sel.xpath('//p[@class="fs14 lh20 c5e slider-area-js"]').xpath('string(.)').extract()[0].strip()

            floor_table = sel.xpath('//div[@class="info-floor floor-data posr clearfix"]//span/text()').extract()
            item['gender'] = floor_table[1]

            hobbie_list = sel.xpath('//div[@class="info-floor floor-hobby posr clearfix"]//span/text()').extract()
            hobbie = {}
            while (hobbie_list):
                hobbie2 = hobbie_list.pop()
                hobbie1 = hobbie_list.pop()
                hobbie[hobbie1] = hobbie2
            item['hobbies'] = hobbie


            mate_sele_list = sel.xpath('//div[@class="info-floor floor-term posr clearfix"]//span/text()').extract()

            mate_sele = {}
            while (mate_sele_list):
                mate_sele2 = mate_sele_list.pop()
                mate_sele1 = mate_sele_list.pop()
                mate_sele[mate_sele1] = mate_sele2

            item['mate_sele_standards'] = mate_sele

        except:
            traceback.print_exc()
        return item

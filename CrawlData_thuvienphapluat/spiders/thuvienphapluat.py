import scrapy
from bs4 import BeautifulSoup
import json
import pymongo
from decouple import config
url = config('url')
client = pymongo.MongoClient(url)
db = client["sonnees"]

def removeLinkTag(links):
    for i in links:
        if(i.startswith("/phap-luat/tag/")):
            links.remove(i)
    return links

def cleanText(text):
    text = text.strip()
    text = text.replace("\n", "")
    text = text.replace("\r", "")
    return text

class ThuvienphapluatSpider(scrapy.Spider):
    name = "thuvienphapluat"
    start_urls = ["https://thuvienphapluat.vn/phap-luat/bat-dong-san?page={}".format(i) for i in range(1)]
    print("Start URL: ", start_urls)

    def parse(self, response):
        links = response.css('article a::attr("href")').getall()
        links = removeLinkTag(links)
        
        for index, link in enumerate(links):
            yield scrapy.Request(url="https://thuvienphapluat.vn"+link, callback=self.parse_detail_article)

    def parse_detail_article(self, response):
        url = response.request.url
        html = response.text
        soup = BeautifulSoup(html, features="lxml")
        title = soup.find("h1").text
        introduction = cleanText(soup.find("strong",{"class": "d-block mt-3 mb-3 sapo"}).text)
        
        title_content = soup.find_all("h2")
        content = []
        for index, h2_tag in enumerate(title_content):
            siblings = h2_tag.find_next_siblings()

            sub_content = []
            for sibling in siblings:
                if sibling.name == 'h2':
                    break
                if(sibling.name == 'p'):
                    if(sibling.find("img")):
                        sub_content.append(sibling.find("img")['src'])
                    else: sub_content.append(cleanText(sibling.text))
                if(sibling.name == 'blockquote'):
                    from_law=[]
                    ems = sibling.find_all("em")
                    for em in ems:
                        from_law.append(em.text)
                    sub_content.append(from_law)
                if(sibling.name == 'a'):
                    continue

            content.append({
                "sub_title": h2_tag.find("strong").text,
                "sub_content": sub_content
            })
        yield {
            "url": url,
            "title": str(title),
            "introduction" : str(introduction),
            "content" : content,
        }

        # result =  {
        #     "url": url,
        #     "title": str(title),
        #     "introduction" : str(introduction),
        #     "content" : content,
        # }
        # while True:
        #     insert_result = db.thuvienphapluat.insert_one(result)
        #     inserted_id = insert_result.inserted_id
        #     if(inserted_id):
        #         break
        
        # with open('output.json', 'a', encoding='utf-8') as json_file:
        #     json.dump(result, json_file, ensure_ascii=False)
        #     json_file.write(',\n')  

# 07/02/2024 by ilmin cho
# KakaoTech AI, Day2
# Crawling
# Request, http요청 라이브러리 → Beautifulsoup html파싱 → Scrapy 크롤링 스크래핑 프레임워크 (정적)→ Selenium 웹 브라우저 자동화 라이브러리 (동적)

# Part 1

#나무위키 정적 데이터 크롤링
#https://realpython.com/python-requests/
#https://pypi.org/project/beautifulsoup4/

'''
import requests
from bs4 import BeautifulSoup
import json

# 요청할 URL
url = "https://namu.wiki/w/%EB%8B%AC%EB%A6%AC%EA%B8%B0"

# 페이지 요청
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
if response.status_code == 200:
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.content, 'html.parser')

    # 크롤링할 데이터 찾기 (예: 제목과 첫 번째 문단)
    title = soup.find('h1').get_text(strip=True)
    paragraphs = soup.find_all('p')

    # 첫 번째 문단 추출
    if paragraphs:
        first_paragraph = paragraphs[0].get_text(strip=True)
    else:
        first_paragraph = "No paragraph found."

    # 크롤링한 데이터 딕셔너리로 저장
    data = {
        "title": title,
        "first_paragraph": first_paragraph
    }

    # 크롤링한 데이터 터미널에 프린트
    print(json.dumps(data, indent=4, ensure_ascii=False))

    # JSON 파일로 저장
    with open('달리기_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
'''



# Part 2

# Kaggle은 JavaScript로 데이터를 동적으로 로드하기 때문에 requests와 BeautifulSoup로는 한계가 있지만 메타 태그에서 유용한 정보를 가져올 수 있다.
# https://stackoverflow.com/questions/36768068/get-meta-tag-content-property-with-beautifulsoup-and-python
'''
import requests
from bs4 import BeautifulSoup
import json

# 요청할 URL
url = "https://www.kaggle.com/datasets/jguerreiro/running"

# 페이지 요청
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
if response.status_code == 200:
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.content, 'html.parser')

    # 메타 태그에서 제목과 설명 추출
    title = soup.find('meta', property='og:title')['content'] if soup.find('meta', property='og:title') else 'No title found'
    description = soup.find('meta', property='og:description')['content'] if soup.find('meta', property='og:description') else 'No description found'

    # 크롤링한 데이터 딕셔너리로 저장
    data = {
        "title": title,
        "description": description
    }

    # 크롤링한 데이터 터미널에 프린트
    print(json.dumps(data, indent=4, ensure_ascii=False))

    # JSON 파일로 저장
    with open('running_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
'''


# Part 3
# Scrapy를 사용하여 Kaggle페이지에서 메타 태그 정보를 크롤링, 이를 JSON 파일에 저장
# https://www.geeksforgeeks.org/how-to-run-scrapy-spiders-in-python/
# https://docs.scrapy.org/en/latest/intro/tutorial.html

import scrapy
import json

class KaggleSpider(scrapy.Spider):
    name = "kaggle"
    start_urls = [
        'https://www.kaggle.com/datasets/jguerreiro/running',
    ]

    def parse(self, response):
        # 메타 태그에서 제목과 설명 추출
        title = response.css('meta[property="og:title"]::attr(content)').get(default='No title found')
        description = response.css('meta[property="og:description"]::attr(content)').get(default='No description found')
        
        yield {
            'title': title,
            'description': description,
        }

class KaggleCrawlerPipeline:
    def open_spider(self, spider):
        self.file = open('running_data.json', 'w', encoding='utf-8')
        self.file.write('[')

    def close_spider(self, spider):
        self.file.seek(self.file.tell() - 2, 0)
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

# Scrapy 설정
# USER_AGENT: 웹사이트들은 스크래핑 요청을 차단하거나 제한함, USER_AGENT를 설정하여 스크래핑 요청을 실제 브라우저에서 오는 요청처럼 보이게함
# ITEM_PIPELINES: 이는 데이터 처리 파이프라인을 지정함, 파이프라인은 크롤링된 데이터를 JSON 파일로 저장하는 역할함. 이 설정이 없으면, 데이터가 파이프라인을 거쳐 파일로 저장되지 않습니다.
settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'ITEM_PIPELINES': {
        '__main__.KaggleCrawlerPipeline': 300,
    }
}

# 크롤러 실행
if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess(settings)
    process.crawl(KaggleSpider)
    process.start()
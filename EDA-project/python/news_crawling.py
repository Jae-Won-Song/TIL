# 필수 라이브러리 호출
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 기사 키값 가져오기
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# 서칭타임 정해주기
import time
from time import sleep  

# 크롤링
from bs4 import BeautifulSoup
import requests

# 크롬드라이버 불러오기
driver = webdriver.Chrome()

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



# 웹페이지 주소 이동
driver.implicitly_wait(10) # 웹페이지가 로딩 될때까지 기다리는 시간
# driver.maximize_window() # 화면 최대화

# 웹페이지 이동 주소 (2010.01.01~ 2023.02.15까지의 기사)

search_stock = input('종목검색 : ')
driver.get("https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q='search_stock'&period=u&sd=20100101000000&ed=20230215235959&p=1&sort=old") 

# 가장 위쪽 페이지로 이동
driver.execute_script("window.scrollTo(0, 0)")

# 페이지 로딩시간 
time.sleep(5)

# 페이지 높이 계산
scroll_height = driver.execute_script("return window.innerHeight")

while True:
    # 한페이지씩 스크롤 다운
    driver.execute_script(f"window.scrollBy(0, {scroll_height})")

    # 페이지 로딩시간 (3초)
    time.sleep(3)

    # 페이지가 끝에 다다르면 멈춤
    new_scroll_height = driver.execute_script("return window.innerHeight")
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height


# 해당 뉴스 제목에서 키워드 추출

def news_title():
    articles = driver.find_elements(By.XPATH, ('/html/body/article/article/div/article/div/div[2]/div[1]/div[1]/ul/li[1]/div[2]/a'))[:30]

    for article in articles:
        title = article.find_elements(By.XPATH, ('.//a')).text
        link = article.find_elements(By.XPATH,('.//a').get_attribute('href'))
        print(title, link)


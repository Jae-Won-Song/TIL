# 필수 라이브러리 호출
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 기사 키값 가져오기
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# 서칭타임 정해주기
import time

# 크롤링
from bs4 import BeautifulSoup
import requests


# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 에러 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
time.sleep(5)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 주소 이동
driver.implicitly_wait(2) # 웹페이지가 로딩 될때까지 기다리는 시간
driver.maximize_window() # 화면 최대화

# 웹페이지 이동 주소
browser = driver.get("https://finance.daum.net/domestic/market_cap") 

# 시총순위 1~50, 기사는 100개 크롤링

# 시총 순위 별 종목 크롤링


# 원하는 종목으로 url이동(XPATH 사용)
url_enter = driver.find_element(By.XPATH, '//*[@id="boxMarketCap"]/div[2]/div/table/tbody/tr[1]/td[2]/a').click()
time.sleep(3)


# 스크롤 내리기

# 초기 스크롤 높이

scroll_height = driver.execute_script("return window.innerHeight")

while True:
    # 한 칸씩 스크롤
    driver.execute_script(f"window.scrollBy(0, {scroll_height})")

    # 대기 1초 (로딩으로 인해 알맞는 초 조절)
    time.sleep(1)

    # 스크롤 길이 비교로 끝까지 갔는지 확인
    new_scroll_height = driver.execute_script("return window.innerHeight")
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height


# 종목 관련 뉴스로 이동
driver.find_element(By.XPATH, '//*[@id="boxTabs"]/td[5]/a').click()



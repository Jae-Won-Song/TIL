from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 에러 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 주소 이동
driver.maximize_window() # 화면 최대화


# 검색어 입력
search_query = '삼성전자'

# Daum Finance 삼성전자 시세 페이지 접속
driver.get('https://finance.daum.net/quotes/A005930#news/market')

# 기사 제목에 키워드가 포함된 경우 페이지 크롤링 후 저장
def crawl_and_save(url):
    driver.get(url)
    # 크롤링 작업 수행
    # ...
    # 결과를 바탕화면에 저장
    result_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'result.txt')
    with open(result_path, 'w') as f:
        f.write('크롤링 결과')

# 뉴스 탭에서 기사 제목과 링크를 가져와 크롤링 수행
while True:
    # 페이지 로딩을 위해 3초 대기
    time.sleep(3)
    
    # 기사 제목과 링크 가져오기
    link_elements = driver.find_elements(By.XPATH, "//ul[@class='list_news']/li/a")
    for link_element in link_elements:
        link = link_element.get_attribute('href')
        if search_query in link_element.text:
            crawl_and_save(link)
            
    # 다음 페이지로 이동
    try:
        next_page_element = driver.find_element(By.XPATH, "//a[@class='btn_page btn_next']")
        next_page_url = next_page_element.get_attribute('href')
        driver.get(next_page_url)
    except:
        break

# 크롬 드라이버 종료
driver.quit()

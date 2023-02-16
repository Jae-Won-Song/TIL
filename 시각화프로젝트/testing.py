import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import lxml.html
# 크롬으로 웹창 시작
browser = webdriver.Chrome()
# 증권 데이터 url 정의
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)
## 조회 항목 초기화
# 체크박스 해제
checkboxes = browser.find_elements(By.NAME, 'fieldIds')  # elements 와 element 오류 발생
for checkbox in checkboxes:
    if checkbox.is_selected(): # 체크박스가 되어 있다면, 해제
        checkbox.click()
# 원하는 항목 체크
wana_checkboxes = ['거래량','고가','저가','ROA']  # 내가 원하는 항목 list
for checkbox in checkboxes:
    top = checkbox.find_element(By.XPATH, '..')     # 부모 class 접근
    bottom = top.find_element(By.TAG_NAME, 'label') # 자식 label 접근
    # print(bottom.text)  체크박스 리스트 확인
    if bottom.text in wana_checkboxes:  # 체크박스리스트와 내가 원하는 항목이 이치시
        checkbox.click()                # 체크박스 클릭
# 적용하기 누르기
apply_push = browser.find_element(By.XPATH,'//*[@id="contentarea_left"]/div[2]/form/div/div/div/a[1]/img')
apply_push.click()
## 1~~5페이지 까지 데이터 추출
for idx in range(1,5):
    # 페이지 이동
    browser.get(url + str(idx))  # 데이터 추출할 페이지
    # 데이터 추출
    kospi_df = pd.read_html(browser.page_source)
    kospi_df[1]  # 데이터 추출
    kospi_df_copy = kospi_df.copy()
    kospi_df_copy1 = kospi_df_copy[1]  # z
    kospi_df_copy1.dropna(axis='index', how='all', inplace=True)  # 복사본  모든 행의 요소가 결측치일 경우 행 삭제
    kospi_df_copy1.dropna(axis='columns', how='all', inplace=True)
    # 파일 저장
    kospi_info = 'kospi.csv'
    if os.path.exists(kospi_info):
        kospi_df_copy1.to_csv(kospi_info, encoding='utf-8-sig', index=False, mode='a', header=False)
    else: # 파일이 없다면
        kospi_df_copy1.to_csv(kospi_info, encoding='utf-8-sig', index=False)
    print(f'{idx} 페이지 완료')
# 1페이지로 이동
browser.get(url)
samsung = browser.find_element(By.XPATH,'//*[@id="contentarea"]/div[3]/table[1]/tbody/tr[2]/td[2]/a')
samsung.click()
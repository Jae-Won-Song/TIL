# selenium ver4

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Key값을 넣기 위함
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('.//chromedriver.exe')
driver.get('https://www.google.co.kr/imghp?hl=ko&ogbl')

# time.sleep(2.3)
# driver.refresh()


# time.sleep(1.3)
elem = driver.find_element(By.NAME, "JW")
elem.clear()
elem.send_keys("pycon")

time.sleep(1.3)
elem.send_keys(Keys.RETURN) # enter키를 친다.

## CSS_selector에 따른 elements 찾기
images = driver.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd' )

# JavaScript와 연결된 코드
SCROLL_PAUSE_TIME = 1.8

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR, '.mye4qd').click()
        except:
            break
    last_height = new_height

cnt = 1
for img in images:
    try:
        time.sleep(2.3)
        img.click()    
        # image 주소 가져오기
        img_url = driver.find_element(By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img' ).get_attribute('src')
            # image 다운로드
        import urllib.request
        urllib.request.urlretrieve(img_url, './test_img/test{0}.png'.format(cnt))
        cnt = cnt + 1
    except:
        pass


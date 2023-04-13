import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/index'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rank_list = soup.select('.realtime .list li')
for rank in rank_list:
    title = rank.select_one('a.title').text.strip()
    author = rank.select_one('a.author').text.strip()
    print(title, author)

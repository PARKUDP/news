from urllib import request
from bs4 import BeautifulSoup
from collections import Counter
import re

url = 'https://news.yahoo.co.jp/topics/top-picks'

# ページの内容を取得
response = request.urlopen(url)
soup = BeautifulSoup(response)

test_one = soup.find('nav', class_='sc-bBXrwG immAzn')
print(soup)
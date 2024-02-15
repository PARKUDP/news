import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

# ウェブページのURL
url = 'https://news.yahoo.co.jp/topics/top-picks'

# ページの内容を取得
response = requests.get(url)

with open('test.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
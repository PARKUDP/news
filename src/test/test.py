from urllib import request
from bs4 import BeautifulSoup
from collections import Counter
import re

# ウェブページのURL
url = 'https://news.yahoo.co.jp/topics/top-picks'

# ページの内容を取得
response = request.urlopen(url)
soup = BeautifulSoup(response)

test_one = soup.find('script', type='application/ld+json')
print(test_one.text)
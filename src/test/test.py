from urllib import request
from bs4 import BeautifulSoup
from collections import Counter
import re

url = 'https://news.yahoo.co.jp/topics/top-picks'

# ページの内容を取得
response = request.urlopen(url)
soup = BeautifulSoup(response)

script_tag_data = soup.find_all('script')  # すべてのscriptタグを取得
prepare_data = script_tag_data[3] # ニュースのタイトルが入っているデータ


# topicListのところを取得しなければならない。(多分、totalの方が全体的な数で、listにはニュースのタイトルとURLが入っている)

from xml.etree.ElementTree import Comment
import requests
from bs4 import BeautifulSoup
import re



#requestによりurlを私、情報をresに格納
url = "https://news.yahoo.co.jp/ranking/access/news/it-science"
res = requests.get(url)

#bs4にてパーサーを指定しデータ抽出
soup = BeautifulSoup(res.text, "html.parser")
article_title = soup.find_all("div", class_="newsFeed_item_title")
article_title_link = soup.find_all("a", href=re.compile("https://news.yahoo.co.jp/articles/"), class_="newsFeed_item_link")

#得られたリストを整える
title = []
for ttl in article_title:
    sttl = str(ttl)
    new_ttl = sttl[33:-6]
    title.append(new_ttl)

link = []
for article_link in article_title_link:
    got_link = article_link.get("href")
    link.append(got_link)

#記事タイトルと記事のリンクを並べてランキング形式で生成
for i in range(40):
    print(title[i])
    print(link[i])





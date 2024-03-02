import requests
from bs4 import BeautifulSoup
#引用先>> https://note.com/stamp_/n/nd9ab3d346f58


def extract_text_from_url(url):
    #URLからHTMLを取得
    response = requests.get(url)
    html_content = response.text

    #BeautifulSoupを用いてHTMLを解析
    soup = BeautifulSoup(html_content, "html.parser")

    #記事の本文を取得
    article_body = soup.find("div", class_="body-copy")

    #テキストの抽出
    text = article_body.get_text()

    return text


url = "https://news.yahoo.co.jp/pickup/6491558"
text = extract_text_from_url(url)
print(text)

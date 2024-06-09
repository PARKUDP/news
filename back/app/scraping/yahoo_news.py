from urllib import request
from bs4 import BeautifulSoup
from collections import Counter
import re
from collections import ChainMap
from flask import Flask, jsonify, render_template
from flask_cors import CORS  #study/src/main.pyより





def data_inquire(url):
    response = request.urlopen(url)
    soup = BeautifulSoup(response, features="lxml")

    script_tag_data = soup.find_all('script')  # すべてのscriptタグを取得
    prepare_data = script_tag_data[3] # ニュースのタイトルが入っているデータ

    # ニュースのタイトルを取得
    news_title = re.findall(r'"title":".*?"', str(prepare_data))  # ニュースのタイトルを取得
    news_title = [re.sub(r'"title":"', '', i) for i in news_title]  # ニュースのタイトルの前の文字列を削除
    news_title = [re.sub(r'"', '', i) for i in news_title]  # ニュースのタイトルの後の文字列を削除

    # ニュースのURLを取得(処理)
    news_url = re.findall(r'"url":".*?"', str(prepare_data))  # ニュースのURLを取得
    news_url = [re.sub(r'"url":"', '', i) for i in news_url]  # ニュースのURLの前の文字列を削除
    news_url = [re.sub(r'"', '', i) for i in news_url]  # ニュースのURLの後の文字列を削除


    # ニュースのタイトルとURLの必要ない情報を削除
    news_title.remove('主要トピックス一覧')
    news_title.remove('アクセスランキング')
    news_title.remove('コメントランキング')
    news_title.remove('トピックス（主要）')

    for url in news_url:
        if url.find('https://news.yahoo.co.jp/pickup/') == -1:
            news_url.remove(url)

    # ニュースのタイトルとURLをdictで保存する。
    result = dict(zip(news_title, news_url))
    return result

if __name__ == "__main__":
    data_inquire()

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

    script_tag_data = soup.find_all('ul', class_="list-news-line")  # すべてのscriptタグを取得  
    prepare_data = script_tag_data # ニュースのタイトルが入っているデータ
  

    # ニュースから得られたデータを整理
    format_url = 'https://www.cnn.co.jp/archives/'
    news_data = re.findall(r'<a href="([^"]+)">\s*([^<]+)\s*</a>', str(prepare_data)) 
    news_data_list = [list(item) for item in news_data]  # リストinリストの状態でurlとニュースタイトルを保持 ==> news_data_list
    for item_data in news_data_list:  # item_data_listを、[[title, url], [title, url]...]の状態に上書き
        item_data[0] = format_url + item_data[0]
        item_data[1] = item_data[1].replace('\u3000', ' ')
        item_data[0], item_data[1] = item_data[1], item_data[0]


    # titleを別でリストに保存
    news_title = [item_title[0] for item_title in news_data_list]

    # ニュースのURLを別で
    news_url = [item_url[1].replace('archives//', '') for item_url in news_data_list]

    # ニュースのタイトルとURLをdictで保存する。
    result = dict(zip(news_title, news_url))
    return result




if __name__ == "__main__":
    data_inquire()
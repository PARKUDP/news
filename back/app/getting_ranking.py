###### sutdy/src/main.pyよりコードをペースト
###### CORSをimport
###### 

from urllib import request
from bs4 import BeautifulSoup
from collections import Counter
import re
from collections import ChainMap
from flask import Flask, jsonify, render_template
from flask_cors import CORS  #study/src/main.pyより
import scraping
from flask_sqlalchemy import SQLAlchemy
import os


path = os.path.abspath(os.path.dirname(__file__))

#CORSを記述
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.news"   # データベース作成するための種類とファイル名
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # メモリ節約でとりま無効

db = SQLAlchemy(app)

CORS(app)


# DataBaseのclass設定
class News_db(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medium = db.Column(db.String("128"), nullable=False)
    news_data = db.Column(db.JSON, nullable=False)


# yahooニュース表示の設定
@app.route('/news_yahoo')
def json_news_yahoo():
    # トピックス一覧1~100件までのURL
    url_one = 'https://news.yahoo.co.jp/topics/top-picks?page=1'
    url_two = 'https://news.yahoo.co.jp/topics/top-picks?page=2'
    url_three = 'https://news.yahoo.co.jp/topics/top-picks?page=3'
    url_four = 'https://news.yahoo.co.jp/topics/top-picks?page=4'

    # トピック一覧1~100件までのデータ
    data_one = scraping.yahoo_news.data_inquire(url_one)
    data_two = scraping.yahoo_news.data_inquire(url_two)
    data_three = scraping.yahoo_news.data_inquire(url_three)
    data_four = scraping.yahoo_news.data_inquire(url_four)

    result_data = ChainMap(data_one, data_two, data_three, data_four)
    merged_data = {}
    
    for d in result_data.maps:
        merged_data.update(d)


    # ここでデータベースに保存
    medium = "yahoo"
    new_data = News_db(medium=medium, news_data=merged_data)
    db.session.add(new_data)
    db.session.commit()
    
    
    return jsonify(merged_data) ######## marged_dataをjson形式でreturnに変更


# cnnニュース表示の設定
@app.route('/news_cnn')
def json_news_cnn():
    # トピックス一覧1~90件までのURL
    url_one = 'https://www.cnn.co.jp/archives/'
    url_two = 'https://www.cnn.co.jp/archives/2/'
    url_three = 'https://www.cnn.co.jp/archives/3/'
    url_four = 'https://www.cnn.co.jp/archives/4/'
    url_five = 'https://www.cnn.co.jp/archives/5/'
    url_six = 'https://www.cnn.co.jp/archives/6/'
    url_seven = 'https://www.cnn.co.jp/archives/7/'

    # トピック一覧1~90件までのデータ
    data_one = scraping.cnn_news.data_inquire(url_one)
    data_two = scraping.cnn_news.data_inquire(url_two)
    data_three = scraping.cnn_news.data_inquire(url_three)
    data_four = scraping.cnn_news.data_inquire(url_four)
    data_five = scraping.cnn_news.data_inquire(url_five)
    data_six = scraping.cnn_news.data_inquire(url_six)
    data_seven= scraping.cnn_news.data_inquire(url_seven)

    result_data = ChainMap(data_one, data_two, data_three, data_four, data_five, data_six, data_seven)
    merged_data = {}
    
    for d in result_data.maps:
        merged_data.update(d)

    
    # ここでデータベースに保存
    medium = "cnn"
    new_data = News_db(medium=medium, news_data=merged_data)
    db.session.add(new_data)
    db.session.commit()

    
    return jsonify(merged_data)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    #app.run(debug=True)

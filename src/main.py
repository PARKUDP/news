from urllib import request
from bs4 import BeautifulSoup
from collections import Counter
import re
from collections import ChainMap
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/news')
def json_news_data():
    # トピックス一覧1~100件までのURL
    url_one = 'https://news.yahoo.co.jp/topics/top-picks?page=1'
    url_two = 'https://news.yahoo.co.jp/topics/top-picks?page=2'
    url_three = 'https://news.yahoo.co.jp/topics/top-picks?page=3'
    url_four = 'https://news.yahoo.co.jp/topics/top-picks?page=4'

    # トピック一覧1~100件までのデータ
    data_one = data_inquire(url_one)
    data_two = data_inquire(url_two)
    data_three = data_inquire(url_three)
    data_four = data_inquire(url_four)

    result_data = ChainMap(data_one, data_two, data_three, data_four)
    merged_data = {}
    for d in result_data.maps:
        merged_data.update(d)
    
    # 変換したdictをJSON化して返す
    return jsonify(merged_data)

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

if __name__ == '__main__':
    app.run(debug=True)
    json_news_data()
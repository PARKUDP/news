from newspaper import Article

url = "https://news.yahoo.co.jp/media/yjnews"
atc = Article(url)
atc.download()
atc.parse()

#記事タイトルを取得
title = atc.title
print(title)
#イメージURLを取得
image_url = atc.top_image
print(image_url)
#記事の概要を取得
text = atc.text
print(text)
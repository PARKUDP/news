import requests




url = "https://news.yahoo.co.jp/"
response = requests.get(url)
html = response.text
print(html)
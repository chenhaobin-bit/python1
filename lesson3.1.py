import requests
import re
url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
response = requests.get(url, headers=headers)
html = response.text
pattern = re.compile(r'<span class="title">([^&]*?)</span>', re.S)
movie_names = pattern.findall(html)
names = [name for name in movie_names if name]
top10 = names[:10]
for i, movie in enumerate(top10, 1):
    print(f"第{i}名：{movie}")
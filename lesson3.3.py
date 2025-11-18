import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    " AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/98.0.4758.102 Safari/537.36"
}
url = "https://movie.douban.com/top250" 
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select(".grid_view li")[:10]
for i, movie in enumerate(movies, 1):
    name = movie.select_one(".title").get_text().strip() 
    info_p = movie.select_one(".bd p").get_text().strip()
    info_line = info_p.split("\n")[1].strip()
    time, country, genre = [item.strip() for item in info_line.replace("\xa0", " ").split("/")]
    comment = movie.select_one(".quote").get_text().strip()
    print(f"第{i}名：{name}，上映时间：{time}，国家：{country}，类型：{genre}，评论：{comment}")
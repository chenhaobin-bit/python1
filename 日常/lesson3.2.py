from bs4 import BeautifulSoup
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
url = "https://movie.douban.com/top250"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
movies = soup.select(".grid_view li")[:10]
for i, movie in enumerate(movies, 1):
    name = movie.select_one(".title").get_text()
    comment = movie.select_one(".quote ").get_text()
    print(f"第{i}名：{name}，评论：{comment}")
    # import requests
# from bs4 import BeautifulSoup
# url = "https://movie.douban.com/top250"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
# }
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")
# ol = soup.find("ol",class_= "grid_view")
# rows = ol.find_all("li")[0:11]
# i = 0
# for row in rows:
#     i = i + 1
#     name = row.find("span",class_= "title").text.strip()
#     cc = row.find("div",class_="bd").find("br").next_sibling.strip()
#     p = cc.split()
#     relseae_time = 
#     # release_time = p[0]
#     # country = p[1]
#     # genre = p[2:]
#     comment = row.find("p",class_="quote").find("span").text.strip()
#     print(f"第{i}名：电影名称：{name},上映时间：{release_time},所属国家：{country},电影类型：{genre},电影评论：{comment}")
import requests
from bs4 import BeautifulSoup as bf
def getHtml(url):
    try:
        r = requests.get(url,timeout=30)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = 'utf-8'
        print(r)
        # print(r.text)
        return r.text
    except:
        print("Wrong")
        return "Wrong"
url = "https://www.shanghairanking.cn/rankings/bcur/202511"
html = getHtml(url)
soup = bf(html,"html.parser")
table = soup.find("table",class_= "rk-table")
rows = table.find_all("tr")[1:11]
print("排名\t学校名称\t省市\t类型\t总分\t办学层次")
for row in rows:
    cols = row.find_all("td")
    rank = cols[0].text.strip()
    name = cols[1].find("span",class_="name-cn").text.strip()
    province = cols[2].text.strip()
    type = cols[3].text.strip()
    score = cols[4].text.strip()
    level = cols[5].text.strip()
    print(f"{rank}\t{name}\t{province}\t{type}\t{score}\t{level}")
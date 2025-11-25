import requests
base = 'https://www.bing.com/'
res = requests.get(url=base)
res.encoding = 'utf-8'
print(res)


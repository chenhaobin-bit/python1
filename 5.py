import requests
re = requests.get('https://www.baidu.com/')
htmltext = re.text
print(htmltext)
with open('baidu.txt','w',encoding="utf-8") as cc :
    cc.write(htmltext)
from bs4 import BeautifulSoup
with open('baidu.txt','r',encoding="utf-8") as cc :
    xx = cc.read()
ss = BeautifulSoup(xx,'html.parser')
title = ss.title
print(title.get_text())
parents = title.parent
print(parents.name)
print(parents.attrs)
tag = ss.form
print(tag.attrs)
print(title.string)
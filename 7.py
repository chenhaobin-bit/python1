import jieba
text = "制定支持数字经济高质量发展政策，积极推进数字产业化、产业数字化，促进数字技术和实体经济深度融合。深化大数据、人工智能等研发应用，开展“人工智能+”行动，打造具有国际竞争力的数字产业集群。实施制造业数字化转型行动，加快工业互联网规模化应用，推进服务业数字化，建设智慧城市、数字乡村。深入开展中小企业数字化赋能专项行动。支持平台企业在促进创新、增加就业、国际竞争中大显身手。健全数据基础制度，大力推动数据开发开放和流通使用。适度超前建设数字基础设施，加快形成全国一体化算力体系，培育算力产业生态。我们要以广泛深刻的数字变革，赋能经济发展、丰富人民生活、提升社会治理现代化水平。"
words = jieba.lcut(text)
fl = [word for word in words if len(word) > 1 ]
worddict = {}
for word in fl:
    if word in worddict:
        worddict[word] += 1
    else:
        worddict[word] = 1
top = sorted(worddict.items(),key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = top[i]
    print(f"{word}:{count}")
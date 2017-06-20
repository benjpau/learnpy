# -*- coding:utf-8 -*-

f = open('text.txt', 'r')
content = f.read().lower()
dic = {}
start = 0
end = 0
flag = 0
for i in range(0, len(content)):
    if content[i].isalpha():
        if flag == 0:
            flag = 1
            start = i
    else:
        if flag == 1:
            flag = 0
            end = i
            word = content[start:end]
            dic.setdefault(word, 0)     # dic默认初始化，若word则什么也不做
            dic[word] += 1
ans = sorted(dic.items(), key=lambda d: d[1], reverse=True)     # 按照value排序，items()将dic转换为list
for it in ans:
    print(str(it[0]) + ':' + str(it[1]))



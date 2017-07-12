# -*- coding:utf-8 -*-
import re


def count_words(path):
    with open(path, 'r') as f:
        content = f.read().lower()
        pattern = re.compile(r'[a-zA-z0-9]+')   # 正则
        words = pattern.findall(content)
        dic = {}
        for word in words:
            dic.setdefault(word, 0)
            dic[word] += 1
        ans = sorted(dic.items(), key=lambda d: d[1], reverse=True)  # 按照value排序，items()将dic转换为list
        for it in ans:
            print(str(it[0]) + ':' + str(it[1]))
    return

if __name__ == '__main__':
    count_words('text.txt')

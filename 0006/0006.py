# -*- coding:utf-8 -*-
import re
import os
FREQ_USED_WORDS = ('and', 'the', 'can', 'a', 'i', 'he', 'him', 'she', 'her', 'we', 'our', 'to', 'of', 'is', 'in')


def find_key_word(directory):
    for file_name in os.listdir(directory):
        with open(os.path.join(directory, file_name), 'r') as file:
            content = file.read().lower()
            pattern = re.compile(r'[a-zA-Z0-9]+')
            words = pattern.findall(content)
            dic = {}
            for word in words:
                dic.setdefault(word, 0)
                dic[word] += 1
            ans = sorted(dic.items(), key=lambda d: d[1], reverse=True)
            for it in ans:
                if it[0] not in FREQ_USED_WORDS:
                    print('Key word of ' + file_name + ' is ' + it[0])
                    break


if __name__ == '__main__':
    find_key_word('diary')
# -*- coding:utf-8 -*-
import codecs
import os


def count_lines(dir_path):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for filename in os.listdir(dir_path):
        with codecs.open(os.path.join(dir_path, filename), 'r', 'utf-8') as file:
            for line in file.read().split('\r\n'):
                cnt1 += 1
                if line.strip().startswith('#'):
                    cnt2 += 1
                elif len(line.strip()) == 0:
                    cnt3 += 1
    print('There are %s lines, %s empty lines, %s notes' % (cnt1, cnt3, cnt2))


if __name__ == '__main__':
    count_lines('code')

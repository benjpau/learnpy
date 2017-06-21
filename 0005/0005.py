# -*- coding:utf-8 -*-
from PIL import Image
import os
# 1136*640


def change_image_res(dir):
    if not os.path.exists('changed'):   # 目录不存在
        os.mkdir('changed')     # 新建文件夹
    for file in os.listdir(dir):
        img = Image.open(os.path.join(dir, file))
        w, h = img.size
        while w > 1136 or h > 640:
            w //= 2
            h //= 2
            img.thumbnail((w, h))   # 缩放图片
        img.save(os.path.join('changed', file), 'jpeg')

if __name__ == '__main__':
    change_image_res('pictures')


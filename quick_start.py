#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Author: JinYu@20866
# File: quick_start.py
# Version: 1.0
# Time: 2024/11/03
# Desc: 将给出的彩色片转换为字符图。
# Website: https://github.com/wephiles
# Copyright: Copyright © 2024 by JinYu@20866, All rights reserved.

"""
How to use:
    >>> python3 quick_start.py --width 80 --height 80 --output ~/show.txt test.png 
"""


from PIL import Image
import argparse

# 命令行输出参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度图映射到70个字符中
def get_char(r, g, b, alpha=256):
    """将灰度图值转换为字符值
    
    Args:
        r ():
        g ():
        b ():
        alpha ():

    Returns:
        int -- A index from 0 to 69!
    """
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(r * 0.299 + g * 0.587 + b * 0.114)

    unit = (256.0 + 1) / length  # 0 ~ 255 共256个 256 + 1 / 70 表示 每一个灰度能表示的RGB值
    return ascii_char[int(gray / unit)]  #找到应该用哪个字符表示这个灰度值



if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ''

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    if OUTPUT:
        with open(OUTPUT, 'w') as fp:
            fp.write(txt)
    else:
        with open('output.txt', 'w') as ffp:
            fp.write(txt)

# --END--


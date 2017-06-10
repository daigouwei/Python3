#!/usr/bin/env
#-*- coding:utf-8 -*-

# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont, ImageColor

def addNum(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('Arial.ttf', size=40)
    fillcolor = ImageColor.colormap.get('red')
    width, height = img.size
    draw.text((width-30, 0), '2', font=myfont, fill=fillcolor)
    img.save('/home/guowei/Downloads/qq.jpg')
    return 0

if __name__ == '__main__':
    image = Image.open('/home/guowei/Downloads/malu.jpg')
    # image = Image.open('~/Downloads/malu.jpg')
    addNum(image)


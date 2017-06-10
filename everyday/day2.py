#!/usr/bin/env
#-*- coding:utf-8 -*-

# Apple Store App 独立开发者，你要搞限时促销，为你的应用生成200个激活码（或者优惠券）。

import uuid

def createNum(num, length=16):
    result = []
    while num>0:
        uuidId = uuid.uuid1()
        temp = str(uuidId).replace('-', '')[:length]
        if temp not in result:
            result.append(temp)
            num -= 1
    return result

if __name__ == '__main__':
    # print(createNum(200))
    print(createNum(200, 6))

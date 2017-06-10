#!/usr/bin/env
#-*- coding:utf-8 -*-

# 作为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 生成 200 个激活码（或者优惠券），并将激活码保存到 Redis 非关系型数据库中。

import uuid
import redis

def createNum(num, length=16):
    result = []
    while num>0:
        uuidId = uuid.uuid1()
        temp = str(uuidId).replace('-', '')[:length]
        if temp not in result:
            result.append(temp)
            num -= 1
    return result

def saveToRedis(numList):
    r = redis.Redis(host='localhost', port=6379, db=0)
    for code in numList:
        r.lpush('code', code)

if __name__ == '__main__':
    saveToRedis(createNum(200))

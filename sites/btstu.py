# coding:utf-8

'''
搏天 API
Home: https://api.btstu.cn/doc/sjbz.php
'''

from imgapi import ImageAPI, Request
import random


lx = [
    'dongman',
    'fengjing'
]


def auto(req: Request):
    return f'https://api.btstu.cn/sjbz/api.php?lx={random.choice(lx)}&method=zsy&format=images'


def horizontal(req: Request):
    return f'https://api.btstu.cn/sjbz/api.php?lx={random.choice(lx)}&method=pc&format=images'


def vertical(req: Request):
    return f'https://api.btstu.cn/sjbz/api.php?lx={random.choice(lx)}&method=mobile&format=images'


api= ImageAPI(
    __name__,
    auto=auto,
    horizontal=horizontal,
    vertical=vertical
)

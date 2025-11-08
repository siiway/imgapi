# coding:utf-8

'''
搏天 API
Home: https://api.btstu.cn/doc/sjbz.php
'''

from imgapi import ImageAPI
import random


lx = [
    'dongman',
    'fengjing'
]


api = ImageAPI(
    __name__,
    auto=lambda req: f'https://api.btstu.cn/sjbz/api.php?lx={random.choice(lx)}&method=zsy&format=images',
    horizontal=lambda req: f'https://api.btstu.cn/sjbz/api.php?lx={random.choice(lx)}&method=pc&format=images',
    vertical=lambda req: f'https://api.btstu.cn/sjbz/api.php?lx={random.choice(lx)}&method=mobile&format=images'
)

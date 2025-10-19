# coding:utf-8

'''
栗次元 API
Home: https://t.alcy.cc/
发布页: https://t.mwm.moe/
Blog: https://www.alcy.cc/archives/sui-ji-er-ci-yuan-tu-pian-api
'''

from imgapi import ImageAPI, Request
from random import choice


catgs_a = ['ycy', 'moez', 'ai', 'ysz']
catgs_h = ['pc', 'moe', 'fj', 'bd', 'ys']
catgs_v = ['mp', 'moemp', 'ysmp', 'aimp']
# `acg` 为动图 / `tx` 为头像方图，故不添加


def auto(req: Request):
    catg = choice(catgs_a)
    return f'https://t.alcy.cc/{catg}/'


def horizontal(req: Request):
    catg = choice(catgs_h)
    return f'https://t.alcy.cc/{catg}/'


def vertical(req: Request):
    catg = choice(catgs_v)
    return f'https://t.alcy.cc/{catg}/'


api = ImageAPI(
    __name__,
    auto=auto,
    horizontal=horizontal,
    vertical=vertical
)

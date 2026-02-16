# coding:utf-8

'''
栗次元 API
Home: https://t.alcy.cc/
发布页: https://t.mwm.moe/
Blog: https://www.alcy.cc/archives/sui-ji-er-ci-yuan-tu-pian-api
'''

from imgapi import ImageAPI
from random import choice

catgs_a = ['ycy', 'moez', 'ai', 'ysz']
catgs_h = ['pc', 'moe', 'fj', 'bd', 'ys']
catgs_v = ['mp', 'moemp', 'ysmp', 'aimp']
# `acg` 为动图 / `tx` 为头像方图，故不添加

api = ImageAPI(
    __name__,
    auto=lambda _: f'https://t.alcy.cc/{choice(catgs_a)}/',
    horizontal=lambda _: f'https://t.alcy.cc/{choice(catgs_h)}/',
    vertical=lambda _: f'https://t.alcy.cc/{choice(catgs_v)}/',
    cn=True,
    outseas=True
)

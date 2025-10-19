# coding:utf-8

'''
牛肉随机图
powered by xiaoyuan
'''

from imgapi import ImageAPI, Request


def auto(req: Request):
    return 'https://img.xiaoyuan151.net/neuro'


api = ImageAPI(
    __name__,
    auto=auto,
    horizontal=auto,
    vertical=auto
)

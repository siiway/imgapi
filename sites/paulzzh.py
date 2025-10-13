# coding:utf-8

'''
Paulzzh API
Home: https://img.paulzzh.com/
API: https://img.paulzzh.com/touhou/random
'''

from imgapi import ImageAPI, Request


def horizontal(req: Request):
    return 'https://img.paulzzh.com/touhou/random?site=all&size=pc'


def vertical(req: Request):
    return 'https://img.paulzzh.com/touhou/random?site=all&size=wap'


api = ImageAPI(
    __name__,
    horizontal=horizontal,
    vertical=vertical
)

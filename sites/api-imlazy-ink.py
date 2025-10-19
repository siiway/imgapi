# coding:utf-8

'''
Imlazy API
Home: https://api.imlazy.ink
Horizonta API: https://api.imlazy.ink/img
Vertical API: https://api.imlazy.ink/img-phone
'''

from imgapi import ImageAPI, Request


def horizontal(req: Request):
    return 'https://api.imlazy.ink/img'


def vertical(req: Request):
    return 'https://api.imlazy.ink/img-phone'


api = ImageAPI(
    __name__,
    horizontal=horizontal,
    vertical=vertical
)

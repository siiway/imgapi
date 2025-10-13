# coding:utf-8

'''
夏沫博客 API
Home: https://cdn.seovx.com/
'''

from imgapi import ImageAPI, Request


def horizontal(req: Request):
    return 'https://cdn.seovx.com/d/?mom=302'


api = ImageAPI(
    __name__,
    horizontal=horizontal
)

# coding:utf-8

'''
墨天逸 API
Home: https://api.mtyqx.cn/
API: https://api.mtyqx.cn/api/random.php
'''

from imgapi import ImageAPI, Request


def horizontal(req: Request):
    return 'https://api.mtyqx.cn/api/random.php'


api = ImageAPI(
    __name__,
    horizontal=horizontal
)

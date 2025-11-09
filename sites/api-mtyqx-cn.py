# coding:utf-8

'''
墨天逸 API
Home: https://api.mtyqx.cn/
API: https://api.mtyqx.cn/api/random.php
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    horizontal=lambda _: 'https://api.mtyqx.cn/api/random.php'
)

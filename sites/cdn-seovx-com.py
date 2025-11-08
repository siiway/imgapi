# coding:utf-8

'''
夏沫博客 API
Home: https://cdn.seovx.com/
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    horizontal=lambda r: 'https://cdn.seovx.com/d/?mom=302'
)

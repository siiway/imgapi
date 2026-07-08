# coding:utf-8

'''
furry.ist 随机福瑞
Home: https://api.furry.ist/
直接返回一张随机兽装/福瑞图片 (SFW)
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    auto='https://api.furry.ist/furry-img/',
    cn=True,
    outseas=True
)

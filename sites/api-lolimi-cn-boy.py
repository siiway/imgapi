# coding:utf-8

'''
lolimi 帅哥图片
Home: https://api.lolimi.cn/
直接返回一张随机帅哥图片 (SFW)
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    auto='https://api.lolimi.cn/API/boy/api.php',
    cn=True,
    outseas=True
)

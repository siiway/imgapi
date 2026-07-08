# coding:utf-8

'''
lolimi 超甜辣妹壁纸
Home: https://api.lolimi.cn/
直接返回一张随机辣妹壁纸 (SFW)
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    auto='https://api.lolimi.cn/API/xjj/lt.php',
    cn=True,
    outseas=True
)

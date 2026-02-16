# coding:utf-8

'''
赫萝随机图片 API
doc: https://api.horosama.com/
'''

from imgapi import ImageAPI


api = ImageAPI(
    __name__,
    horizontal=lambda _: 'https://api.horosama.com/random.php?type=pc',
    vertical=lambda _: 'https://api.horosama.com/random.php?type=mobile',
    cn=True,
    outseas=True
)

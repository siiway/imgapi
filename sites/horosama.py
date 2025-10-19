# coding:utf-8

'''
赫萝随机图片 API
doc: https://api.horosama.com/
'''

from imgapi import ImageAPI, Request


def horizontal(req: Request):
    return 'https://api.horosama.com/random.php?type=pc'


def vertical(req: Request):
    return 'https://api.horosama.com/random.php?type=mobile'


api = ImageAPI(
    __name__,
    horizontal=horizontal,
    vertical=vertical
)

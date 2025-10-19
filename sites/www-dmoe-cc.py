# coding:utf-8

'''
樱花随机二次元图片 API
doc: https://www.dmoe.cc/
'''

from imgapi import ImageAPI, Request


def horizontal(req: Request):
    return 'https://www.dmoe.cc/random.php'


api= ImageAPI(
    __name__,
    horizontal=horizontal
)

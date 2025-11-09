# coding:utf-8

'''
樱花随机二次元图片 API
doc: https://www.dmoe.cc/
'''

from imgapi import ImageAPI

api= ImageAPI(
    __name__,
    horizontal=lambda _: 'https://www.dmoe.cc/random.php'
)

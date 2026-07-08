# coding:utf-8

'''
Lorem Picsum
Home: https://picsum.photos/
随机摄影图片 (三次元), 指定尺寸直接返回图片
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    horizontal='https://picsum.photos/1920/1080',
    vertical='https://picsum.photos/1080/1920',
    outseas=True
)

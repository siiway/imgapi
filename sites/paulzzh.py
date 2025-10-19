# coding:utf-8

'''
Paulzzh API
Home: https://img.paulzzh.com/
API: https://img.paulzzh.com/touhou/random
测试发现即使请求 ?size=wap 也大概率返回横屏图片，故禁用 vertical
'''

from imgapi import ImageAPI, Request


def horizontal(req: Request):
    return 'https://img.paulzzh.com/touhou/random?site=all&size=pc'


# def vertical(req: Request):
#     return 'https://img.paulzzh.com/touhou/random?site=all&size=wap'


api = ImageAPI(
    __name__,
    horizontal=horizontal,
    # vertical=vertical
)

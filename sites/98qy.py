# coding:utf-8

'''
98情缘API
主站 https://www.98qy.com/sjbz/

'''

from imgapi import ImageAPI, Request


def auto(req: Request):
    return 'https://www.98qy.com/sjbz/api.php?method=zsy'


def horizontal(req: Request):
    return 'https://www.98qy.com/sjbz/api.php?method=pc'


def vertical(req: Request):
    return 'https://www.98qy.com/sjbz/api.php?method=mobile'


api = ImageAPI(
    __name__,
    auto=auto,
    horizontal=horizontal,
    vertical=vertical
)

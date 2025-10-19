# coding:utf-8

'''
保罗 API
Doc: https://api.paugram.com/help/wallpaper
API: https://api.paugram.com/wallpaper/
'''

from imgapi import ImageAPI, Request
from random import choice


src_list = ['sm', 'cp', 'sina', 'paul', 'gh', 'jsd']


def horizontal(req: Request):
    return f'https://api.paugram.com/wallpaper/?type=horizontal&source={choice(src_list)}'


api = ImageAPI(
    __name__,
    horizontal=horizontal
)

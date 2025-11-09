# coding:utf-8

'''
保罗 API
Doc: https://api.paugram.com/help/wallpaper
API: https://api.paugram.com/wallpaper/
'''

from imgapi import ImageAPI
from random import choice


src_list = ['sm', 'cp', 'sina', 'paul', 'gh', 'jsd']


api = ImageAPI(
    __name__,
    horizontal=lambda _: f'https://api.paugram.com/wallpaper/?type=horizontal&source={choice(src_list)}'
)

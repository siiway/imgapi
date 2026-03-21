# coding: utf-8

'''
二叉树树 EO API
Source Repo: https://github.com/afoim/choice_randompic
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    horizontal=lambda _: 'https://c-p.2x.nz/h',
    vertical=lambda _: 'https://c-p.2x.nz/v',
    outseas=True
)

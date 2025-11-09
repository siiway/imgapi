# coding:utf-8

'''
Imlazy API
Home: https://api.imlazy.ink
Horizonta API: https://api.imlazy.ink/img
Vertical API: https://api.imlazy.ink/img-phone
'''

from imgapi import ImageAPI


api = ImageAPI(
    __name__,
    horizontal=lambda _: 'https://api.imlazy.ink/img',
    vertical=lambda _: 'https://api.imlazy.ink/img-phone'
)

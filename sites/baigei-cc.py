# coding: utf-8
'''
baigei的随机图api
Blog Post: https://baigei.cc/index.php/archives/28/
API:
- 芙宁娜: https://furina.baigei.cc/{index,pc,phone}.php
- 昔涟: https://philia093.baigei.cc/{index,pc,phone}.php
'''

from imgapi import ImageAPI

n = False

def roll():
    global n
    if n:
        n = False
        return 'philia093'
    else:
        n = True
        return 'furina'

api = ImageAPI(
    id=__name__,
    horizontal=lambda _: f'https://{roll()}.baigei.cc/pc.php',
    vertical=lambda _: f'https://{roll()}.baigei.cc/phone.php',
    auto=lambda _: f'https://{roll()}.baigei.cc/index.php'
)
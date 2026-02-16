# coding: utf-8

'''
二叉树树 EO API
Blog: https://blog.2b2x.cn/posts/acg-randompic-api/
Auto: https://eopfapi.acofork.com/pic?img=ua
Horizontal: https://eopfapi.acofork.com/pic?img=h
Vertical: https://eopfapi.acofork.com/pic?img=v
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    horizontal=lambda _: 'https://eopfapi.acofork.com/pic?img=h',
    vertical=lambda _: 'https://eopfapi.acofork.com/pic?img=v',
    auto=lambda _: 'https://eopfapi.acofork.com/pic?img=ua',
    cn=True,
    outseas=True
)

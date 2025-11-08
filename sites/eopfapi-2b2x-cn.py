# coding: utf-8

'''
二叉树树 EO API
Blog: https://blog.2b2x.cn/posts/acg-randompic-api/
Auto: https://eopfapi.2b2x.cn/pic?img=ua
Horizontal: https://eopfapi.2b2x.cn/pic?img=h
Vertical: https://eopfapi.2b2x.cn/pic?img=v
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    horizontal=lambda req: 'https://eopfapi.2b2x.cn/pic?img=h',
    vertical=lambda req: 'https://eopfapi.2b2x.cn/pic?img=v',
    auto=lambda req: 'https://eopfapi.2b2x.cn/pic?img=ua'
)

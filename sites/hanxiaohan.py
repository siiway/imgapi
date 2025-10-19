# coding:utf-8

'''
韩小韩 API
docs:
 - Bing: https://api.vvhan.com/article/bing.html
 - 风景: https://api.vvhan.com/article/views.html
 - 二次元: https://api.vvhan.com/article/acg.html
Disabled (多地区超时)
'''

from imgapi import ImageAPI, Request


apis = [
    'https://api.vvhan.com/api/bing',
    'https://api.vvhan.com/api/wallpaper/views',
    # 'https://api.vvhan.com/api/wallpaper/acg' # Disabled because of R18 images
]


def horizontal(req: Request):
    from random import choice
    return choice(apis)


# api = ImageAPI(
#     __name__,
#     horizontal=horizontal
# )

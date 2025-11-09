# coding:utf-8

'''
98情缘API
主站 https://www.98qy.com/sjbz/
API 作者貌似离人有点远了, 三个 method 都只返回横屏图片
'''

from imgapi import ImageAPI, Request


# def auto(req: Request):
#     return 'https://www.98qy.com/sjbz/api.php?method=zsy'


# def horizontal(req: Request):
#     return 'https://www.98qy.com/sjbz/api.php?method=pc'


# def vertical(req: Request):
#     return 'https://www.98qy.com/sjbz/api.php?method=mobile'

async def horizontal(re: Request):
    # 抓包得上面三个都重定向到这
    return 'https://www.98qy.com/sjbz/api2.php'


api = ImageAPI(
    __name__,
    # auto=auto,
    horizontal=horizontal,
    # vertical=vertical
)

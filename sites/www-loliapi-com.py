# coding:utf-8

'''
LoliAPI
Home: https://www.loliapi.com/
随机二次元壁纸, 302 跳转到图片
- 自动(随机): https://www.loliapi.com/bg
- 横向: https://www.loliapi.com/acg/pc
- 竖向: https://www.loliapi.com/acg/pe
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    auto='https://www.loliapi.com/bg',
    horizontal='https://www.loliapi.com/acg/pc',
    vertical='https://www.loliapi.com/acg/pe',
    cn=True,
    outseas=True
)

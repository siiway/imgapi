# coding:utf-8

'''
imgapi.cn 随机图片
Home: https://imgapi.cn/
真人 / 动漫 / 风景 随机图片, 302 跳转到图片
zd: 尺寸 (zsy-默认, pc-横, mobile-竖)
fl: 分类 (suiji-随机, meizi-真人, dongman-动漫, fengjing-风景)
'''

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    auto='https://imgapi.cn/api.php?zd=zsy&fl=suiji',
    horizontal='https://imgapi.cn/api.php?zd=pc&fl=suiji',
    vertical='https://imgapi.cn/api.php?zd=mobile&fl=suiji',
    cn=True,
    outseas=True
)

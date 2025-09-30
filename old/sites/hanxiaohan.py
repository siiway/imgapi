# coding:utf-8

'''
韩小韩 API
docs:
 - Bing: https://api.vvhan.com/article/bing.html
 - 风景: https://api.vvhan.com/article/views.html
 - 二次元: https://api.vvhan.com/article/acg.html
'''

from flask import Blueprint, redirect
from random import choice

allow_s = False
allow_h = True
allow_v = False


site = Blueprint('hanxiaohan', __name__)

apis = [
    'https://api.vvhan.com/api/bing',
    'https://api.vvhan.com/api/wallpaper/views',
    # 'https://api.vvhan.com/api/wallpaper/acg' # Disabled because of R18 images
]


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect(choice(apis))

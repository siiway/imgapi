# coding:utf-8

'''

'''

from flask import Blueprint, redirect
from random import choice

allow_a = False
allow_h = True
allow_v = False


site = Blueprint('hanxiaohan', __name__)

apis = ['https://api.vvhan.com/api/bing',
        'https://api.vvhan.com/api/wallpaper/views',
        'https://api.vvhan.com/api/wallpaper/acg']


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect(choice(apis))

# coding:utf-8

'''
樱花随机二次元图片 API
doc: https://www.dmoe.cc/
'''

from flask import Blueprint, redirect

allow_s = False
allow_h = True
allow_v = False


site = Blueprint('yinghua', __name__)


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect('https://www.dmoe.cc/random.php')

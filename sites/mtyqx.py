# coding:utf-8

'''
墨天逸 API
Home: https://api.mtyqx.cn/
API: https://api.mtyqx.cn/api/random.php
'''

from flask import Blueprint, redirect

allow_s = False
allow_h = True
allow_v = False


site = Blueprint('mtyqx', __name__)


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect('https://api.mtyqx.cn/api/random.php')

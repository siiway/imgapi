# coding:utf-8

'''
搏天 API
Home: https://api.btstu.cn/doc/sjbz.php
'''

from flask import Blueprint, redirect
import random

allow_s = True
allow_h = True
allow_v = True


site = Blueprint('btstu', __name__)

lx = [
    'dongman',
    'fengjing'
]


@site.route('/image')
@site.route('/image/s')
def image_a():
    return redirect(f'https://api.btstu.cn/sjbz/api.php?lx={random.choice(lx)}&method=zsy&format=images')


@site.route('/image/h')
def image_h():
    return redirect(f'https://api.btstu.cn/sjbz/api.php?lx={random.choice(lx)}&method=pc&format=images')


@site.route('/image/v')
def image_v():
    return redirect(f'https://api.btstu.cn/sjbz/api.php?lx={random.choice(lx)}&method=mobile&format=images')

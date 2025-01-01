# coding:utf-8

'''
搏天 API
Home: https://api.btstu.cn/doc/sjbz.php
'''

from flask import Blueprint, redirect
import random

allow_a = True
allow_h = True
allow_v = True


site = Blueprint('', __name__)

lx = random.choice([
    'dongman',
    'fengjing'
])


@site.route('/image')
@site.route('/image/a')
def image_a():
    return redirect(f'https://api.btstu.cn/sjbz/api.php?lx={lx}&method=zsy&format=images')


@site.route('/image/h')
def image_h():
    return redirect(f'https://api.btstu.cn/sjbz/api.php?lx={lx}&method=pc&format=images')


@site.route('/image/v')
def image_v():
    return redirect(f'https://api.btstu.cn/sjbz/api.php?lx={lx}&method=mobile&format=images')

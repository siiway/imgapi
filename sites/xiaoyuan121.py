# coding:utf-8

'''
牛肉随机图
powered by xiaoyuan
'''

from flask import Blueprint, redirect

allow_s = False
allow_h = True
allow_v = False


site = Blueprint('xiaoyuan', __name__)


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect('https://img.xiaoyuan151.com/neuro')
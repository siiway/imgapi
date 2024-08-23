# coding:utf-8

'''
零七生活 API
doc: https://api.oick.cn/doc/random
'''

from flask import Blueprint, redirect

allow_a = False
allow_h = True
allow_v = True


site = Blueprint('lingqi', __name__)


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect('https://api.oick.cn/api/random?type=pc')


@site.route('/image/v')
def image_v():
    return redirect('https://api.oick.cn/api/random?type=pe')

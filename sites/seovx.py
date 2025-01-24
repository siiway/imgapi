# coding:utf-8

'''
夏沫博客 API
Home: https://cdn.seovx.com/
'''

from flask import Blueprint, redirect

allow_a = False
allow_h = True
allow_v = False


site = Blueprint('seovx', __name__)


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect('https://cdn.seovx.com/d/?mom=302')

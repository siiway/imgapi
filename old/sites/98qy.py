# coding:utf-8

'''
98情缘API
主站 https://www.98qy.com/sjbz/

'''

from flask import Blueprint, redirect

allow_s = True
allow_h = True
allow_v = True


site = Blueprint('98qy', __name__)


@site.route('/image')
@site.route('/image/s')
def image_a():
    return redirect('https://www.98qy.com/sjbz/api.php?method=zsy')


@site.route('/image/h')
def image_h():
    return redirect('https://www.98qy.com/sjbz/api.php?method=pc')


@site.route('/image/v')
def image_v():
    return redirect('https://www.98qy.com/sjbz/api.php?method=mobile')

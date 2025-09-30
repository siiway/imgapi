# coding:utf-8

'''
赫萝随机图片 API
doc: https://api.horosama.com/
'''

from flask import Blueprint, redirect

allow_s = False
allow_h = True
allow_v = True


site = Blueprint('horosama', __name__)


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect('https://api.horosama.com/random.php?type=pc')


@site.route('/image/v')
def image_v():
    return redirect('https://api.horosama.com/random.php?type=mobile')

# coding:utf-8

'''

'''

from flask import Blueprint, redirect

allow_a = False
allow_h = True
allow_v = False


site = Blueprint('yinghua', __name__)


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect('https://www.dmoe.cc/random.php')

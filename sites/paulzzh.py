# coding:utf-8

'''
Paulzzh API
Home: https://img.paulzzh.com/
API: https://img.paulzzh.com/touhou/random
'''

from flask import Blueprint, redirect

allow_s = False
allow_h = True
allow_v = True


site = Blueprint('paulzzh', __name__)


@site.route('/image')
@site.route('/image/s')
def image_a():
    return redirect('')


@site.route('/image/h')
def image_h():
    return redirect('')


@site.route('/image/v')
def image_v():
    return redirect('')

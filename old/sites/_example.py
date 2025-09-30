# coding:utf-8

'''
Template
Doc: 
API: 
'''

from flask import Blueprint, redirect

allow_s = True
allow_h = True
allow_v = True


site = Blueprint('', __name__)


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

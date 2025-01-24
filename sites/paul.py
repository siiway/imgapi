# coding:utf-8

'''
保罗 API
Doc: https://api.paugram.com/help/wallpaper
API: https://api.paugram.com/wallpaper/
'''

from flask import Blueprint, redirect
from random import choice

allow_a = False
allow_h = True
allow_v = False


site = Blueprint('paul', __name__)
src_list = ['sm', 'cp', 'sina', 'paul', 'gh', 'jsd']


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect(f'https://api.paugram.com/wallpaper/?source={choice(src_list)}')

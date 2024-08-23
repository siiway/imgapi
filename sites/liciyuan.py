# coding:utf-8

'''
栗次元 API
Home: https://t.alcy.cc/
发布页: https://t.mwm.moe/
Blog: https://www.alcy.cc/archives/sui-ji-er-ci-yuan-tu-pian-api
'''

from utils import format_dict
from flask import Blueprint, redirect
from random import choice

allow_a = True
allow_h = True
allow_v = True


site = Blueprint('liciyuan', __name__)

catgs_a = ['ycy', 'moez', 'ai', 'ysz']
catgs_h = ['pc', 'moe', 'fj', 'bd', 'ys']
catgs_v = ['mp', 'moemp', 'ysmp', 'aimp']
# `acg` 为动图 / `tx` 为头像方图，故不添加


@site.route('/image')
@site.route('/image/a')
def image_a():
    catg = choice(catgs_a)
    return redirect(f'https://t.alcy.cc/{catg}')


@site.route('/image/h')
def image_h():
    catg = choice(catgs_h)
    return redirect(f'https://t.alcy.cc/{catg}')


@site.route('/image/v')
def image_v():
    catg = choice(catgs_v)
    return redirect(f'https://t.alcy.cc/{catg}')

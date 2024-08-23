# coding:utf-8

'''
栗次元 API
Home: https://t.alcy.cc/
发布页: https://t.mwm.moe/
Blog: https://www.alcy.cc/archives/sui-ji-er-ci-yuan-tu-pian-api
'''

from utils import format_dict
import requests
from flask import Blueprint, redirect
from random import choice

allow_json = True
allow_image = True


site = Blueprint('liciyuan', __name__)

catgs = ['ycy', 'moez', 'ai', 'ysz', 'pc', 'moe', 'fj',
         'bd', 'ys', 'lai', 'xhl']

# `acg` 为动图 / `tx` 为头像方图，故不添加
# 'mp', 'moemp', 'ysmp', 'aimp', 竖屏不加


@site.route('/image')
def image():
    catg = choice(catgs)
    return redirect(f'https://t.alcy.cc/{catg}')


@site.route('/json')
def json():
    catg = choice(catgs)
    return redirect(f'https://t.alcy.cc/{catg}?json')

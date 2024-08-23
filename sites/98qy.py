# coding:utf-8

'''
98情缘API
主站 https://www.98qy.com/
图片 https://www.98qy.com/sjbz/

'''

import requests
from flask import Blueprint, redirect

allow_image = True
allow_json = False


site = Blueprint('98qy', __name__)


@site.route('/image')
def image():
    return redirect('https://www.98qy.com/sjbz/api.php')

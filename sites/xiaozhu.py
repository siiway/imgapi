# coding:utf-8

'''
岁月小筑 (二开) 动漫 api
doc: https://cloud.qqshabi.cn/apidetail/33.html
'''

from flask import Blueprint, redirect

allow_a = False
allow_h = True
allow_v = False


site = Blueprint('xiaozhu', __name__)


@site.route('/image')
@site.route('/image/h')
def image_h():
    return redirect('https://cloud.qqshabi.cn/api/images/api.php')

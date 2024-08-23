# !/usr/bin/python3
# coding:utf-8

'''
重要的提示
a -> auto 自适应
h -> horizontal 水平 (横向)
v -> vertical 垂直 (竖向)
'''

import importlib
import os
from flask import Flask, redirect
import config as cfg
import utils as u
from random import choice


app = Flask(__name__)

h_sites_list = []
v_sites_list = []
a_sites_list = []

for n in os.listdir('sites/'):
    name, ext = os.path.splitext(n)
    if ext == '.py' and name != '_example':
        obj = importlib.import_module(f'sites.{name}')
        app.register_blueprint(obj.site, url_prefix=f'/sites/{name}')
        if obj.allow_h:
            h_sites_list += [name]
        if obj.allow_v:
            v_sites_list += [name]
        if obj.allow_a:
            a_sites_list += [name]
        u.info(f'Registered: {name}')

u.debug(f'Allow_horizontal: {h_sites_list}')
u.debug(f'Allow_vertical: {v_sites_list}')
u.debug(f'Allow_auto: {a_sites_list}')


@app.route('/')
def index():
    return redirect('https://github.com/wyf01239/imgapi')


@app.route('/image')
@app.route('/image/a')
def image_a():
    ch = choice(a_sites_list)
    return redirect(f'/sites/{ch}/image/a')


@app.route('/image/h')
def image_h():
    ch = choice(h_sites_list)
    return redirect(f'/sites/{ch}/image/h')


@app.route('/image/v')
def image_v():
    ch = choice(v_sites_list)
    return redirect(f'/sites/{ch}/image/v')


@app.route('/test')
def test():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(
        host=cfg.host,
        port=cfg.port,
        debug=cfg.debug
    )

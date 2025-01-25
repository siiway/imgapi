# !/usr/bin/python3
# coding:utf-8

'''
重要的提示
s -> self 自适应
h -> horizontal 水平 (横向)
v -> vertical 垂直 (竖向)
'''

import importlib
import os
from flask import Flask, redirect, request
from random import choice
from user_agents import parse as parse_ua

import config as cfg
import utils as u

app = Flask(__name__)

h_sites_list = []
v_sites_list = []
s_sites_list = []

sites_count = 0
h_sites_count = 0
v_sites_count = 0
s_sites_count = 0

u.info('Loading: ', noret=True)
dirlst = os.listdir('sites/')
for n in dirlst:
    name, ext = os.path.splitext(n)
    if ext == '.py' and name != '_example':
        obj = importlib.import_module(f'sites.{name}')
        app.register_blueprint(obj.site, url_prefix=f'/sites/{name}')
        if obj.allow_h:
            h_sites_list += [name]
            h_sites_count += 1
        if obj.allow_v:
            v_sites_list += [name]
            v_sites_count += 1
        if obj.allow_s:
            s_sites_list += [name]
            s_sites_count += 1
        sites_count += 1
        print(name, end=', ')

print()
u.info(f'Loaded {sites_count} api(s): {h_sites_count} horizontal, {v_sites_count} vertical, {s_sites_count} self.')

u.debug(f'Allow_horizontal: {h_sites_list}')
u.debug(f'Allow_vertical: {v_sites_list}')
u.debug(f'Allow_self: {s_sites_list}')


@app.route('/')
def index():
    return redirect('https://github.com/siiway/imgapi')


@app.route('/img')
@app.route('/image')
def image_auto():
    ua_str: str = request.headers.get('User-Agent', None)
    if ua_str:
        ua = parse_ua(ua_str)
        if ua.is_mobile:
            # Mobile -> V
            return image_v()
        elif ua.is_pc or ua.is_tablet:
            # PC / Tablet -> H
            return image_h()
        else:
            # Unknown -> S
            return image_s()
    else:
        return image_s()


@app.route('/img/s')
@app.route('/image/s')
def image_s():
    ch = choice(s_sites_list)
    return redirect(f'/sites/{ch}/image/s')


@app.route('/img/h')
@app.route('/image/h')
def image_h():
    ch = choice(h_sites_list)
    return redirect(f'/sites/{ch}/image/h')


@app.route('/img/v')
@app.route('/image/v')
def image_v():
    ch = choice(v_sites_list)
    return redirect(f'/sites/{ch}/image/v')


@app.route('/about')
def about():
    ua_str = request.headers.get('User-Agent', None)
    if ua_str:
        ua_obj = parse_ua(ua_str)
        ua = f'is_mobile: {ua_obj.is_mobile}, is_pc: {ua_obj.is_pc}, is_tablet: {ua_obj.is_tablet}'
        if ua_obj.is_mobile:
            # Mobile -> V
            result = 'Vertical'
        elif ua_obj.is_pc or ua_obj.is_tablet:
            # PC / Tablet -> H
            result = 'Horizontal'
        else:
            # Unknown -> S
            result = 'Self'
    else:
        ua_obj = 'No User-Agent Header'
        result = 'Self'
    return f'''
Hello World! <br/>
SiiWay ImgAPI v2024-01-25 - https://github.com/siiway/imgapi <br/>
Copyright (c) 2025 SiiWay Team. Under MIT License. <br/>
<br/>
--- UA Test --- <br/>
UA String: {ua_str} <br/>
Parsed UA: {ua_obj} - {ua} <br/>
Result -> {result} <br/>
'''


if __name__ == '__main__':
    app.run(
        host=cfg.host,
        port=cfg.port,
        debug=cfg.debug
    )

# !/usr/bin/python3
# coding:utf-8

# bulitin
import importlib
import os
from random import choice

# 3rd-party
from flask import Flask, redirect, request
from user_agents import parse as parse_ua  # type: ignore

# local
import config as cfg

# --- log


def info(msg, noret=False):
    if noret:
        print(f'[I] {msg}', end='')
    else:
        print(f'[I] {msg}')


def warning(msg, noret=False):
    if noret:
        print(f'[W] {msg}', end='')
    else:
        print(f'[W] {msg}')


def error(msg, noret=False):
    if noret:
        print(f'[E] {msg}', end='')
    else:
        print(f'[E] {msg}')


def debug(msg, noret=False):
    if noret:
        print(f'[D] {msg}', end='')
    else:
        print(f'[D] {msg}')
#
# --- app


app = Flask(__name__)

h_sites_list = []
v_sites_list = []
s_sites_list = []

sites_count = 0
h_sites_count = 0
v_sites_count = 0
s_sites_count = 0

info('Loading: ', noret=True)
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

print('OK')
info(f'Loaded {sites_count} api(s): {h_sites_count} horizontal, {v_sites_count} vertical, {s_sites_count} self.')

debug(f'Allow_horizontal: {h_sites_list}')
debug(f'Allow_vertical: {v_sites_list}')
debug(f'Allow_self: {s_sites_list}')


@app.route('/')
def index():
    return redirect('https://github.com/siiway/imgapi')


@app.route('/img')
@app.route('/image')
def image_auto():
    ua_str: str | None = request.headers.get('User-Agent', None)
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
    # UA
    ua_str = request.headers.get('User-Agent')
    if ua_str:
        ua_obj = parse_ua(ua_str)
        # Types
        ua_types = ''
        ua_types += '  - Bot <br/>\n' if ua_obj.is_bot else ''
        ua_types += '  - Email Client <br/>\n' if ua_obj.is_email_client else ''
        ua_types += '  - Mobile <br/>\n' if ua_obj.is_mobile else ''
        ua_types += '  - PC <br/>\n' if ua_obj.is_pc else ''
        ua_types += '  - Tablet <br/>\n' if ua_obj.is_tablet else ''
        ua_types += '  - Touch Capable <br/>\n' if ua_obj.is_touch_capable else ''
        ua_types = ua_types if ua_types else '  - None <br/>'
        # Result
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
        ua_types = 'Unknown'
        result = 'Self'
    # Fwd
    forwarded = request.headers.get('X-Forwarded-For')

    ret = f'''
Hello World! <br/>
SiiWay ImgAPI v2025-05-10 - https://github.com/siiway/imgapi <br/>
Copyright (c) 2025 SiiWay Team. Under MIT License. <br/>
<br/>
----- Visitor ----- <br/>
Host: {request.host} <br/>
IP: {request.remote_addr} <br/>
X-Forwarded-For: {forwarded} <br/>
Origin: {request.origin} <br/>
Referer: {request.referrer} <br/>
<br/>
----- UA Test ----- <br/>
User-Agent: {ua_str} <br/>
Info: <br/>
  - Device: {ua_obj.get_device()} <br/>
  - OS: {ua_obj.get_os()} <br/>
  - Browser: {ua_obj.get_browser()} <br/>
Type: <br/>
{ua_types}
Result: {result} <br/>
'''
    if (not ua_obj.is_pc) and (not ua_obj.is_mobile) and (not ua_obj.is_tablet) and (not ua_obj.is_touch_capable):
        ret = f'{"="*29}\n{ret}\n{"="*29}'.replace('<br/>', '').replace('-----', '----------')
    return ret


if __name__ == '__main__':
    app.run(
        host=cfg.host,
        port=cfg.port,
        debug=cfg.debug
    )

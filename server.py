# !/usr/bin/python3
# coding:utf-8

import importlib
import os
from flask import Flask, redirect
import config as cfg
import utils as u
from random import choice


app = Flask(__name__)

image_sites_list = []
json_sites_list = []

for n in os.listdir('sites/'):
    name, ext = os.path.splitext(n)
    if ext == '.py' and name != '_example':
        obj = importlib.import_module(f'sites.{name}')
        app.register_blueprint(obj.site, url_prefix=f'/sites/{name}')
        if obj.image:
            image_sites_list += [name]
        if obj.json:
            json_sites_list += [name]
        u.info(f'Registered: {name}')

u.debug(f'AllowImage: {image_sites_list}')
u.debug(f'AllowJson: {json_sites_list}')

@app.route('/')
def index():
    return redirect('https://github.com/wyf01239/imgapi')

@app.route('/image')
def image():
    ch = choice(image_sites_list)
    return redirect(f'/sites/{choice}/image')


@app.route('/json')
def json():
    ch = choice(json_sites_list)
    return redirect(f'/sites/{choice}/json')

@app.route('/test')
def test():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(
        host=cfg.host,
        port=cfg.port,
        debug=cfg.debug
    )

#!/usr/bin/python3
# coding:utf-8

import utils as u
import config as cfg
from flask import Flask, render_template, request, url_for, redirect, flash
from markupsafe import escape
import json

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(location='https://github.com/wyf01239/imgapi', code=302)


@app.route('/test')
def test():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(
        host=cfg.host,
        port=cfg.port,
        debug=cfg.debug
    )

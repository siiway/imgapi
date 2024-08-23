# coding:utf-8

'''

'''

from ..utils import format_dict
import requests
from flask import Blueprint, redirect

allow_json = True
allow_image = True


site = Blueprint('', __name__)


@site.route('/image')
def image():
    return redirect('')


@site.route('/json')
def json():
    return format_dict({'a': 'b'})

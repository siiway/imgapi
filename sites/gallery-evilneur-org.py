# coding:utf-8

"""
EvilNeur Gallery
Home: https://gallery.evilneur.org/
API: https://gallery.evilneur.org/random
"""

from imgapi import ImageAPI


api = ImageAPI(
    __name__,
    auto="https://gallery.evilneur.org/random",
    horizontal="https://gallery.evilneur.org/random",
    vertical="https://gallery.evilneur.org/random",
    cn=True,
    outseas=True,
)

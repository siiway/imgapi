"""
YM-API 与末API
Home & Docs: https://img-api.yumo.cc
"""

from random import choice
from imgapi import ImageAPI

elements = ["muse-dash", "hqsw", "ddlc"]

api = ImageAPI(
    __name__,
    horizontal=lambda _: f"https://img-api.yumo.cc/api/{choice(elements)}-bg/",
)
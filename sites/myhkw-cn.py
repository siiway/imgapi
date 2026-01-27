"""
明月浩空网
Home: https://myhkw.cn/

API List:
  - `bing`: Bing 每日壁纸 (每日刷新)
  - `mojave`: 动态莫哈维昼夜图片 (每日刷新)
"""

from random import choice
from imgapi import ImageAPI

entry = ["bing", "mojave"]

api = ImageAPI(
    __name__,
    horizontal=lambda _: f"https://myhkw.cn/open/img/{choice(entry)}",
)

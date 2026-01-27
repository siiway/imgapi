"""
图样跑酷
Home: https://img.run/

Bing 随机壁纸 (非每日刷新)
"""

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    horizontal=lambda _: "https://bing.img.run/rand.php",
)

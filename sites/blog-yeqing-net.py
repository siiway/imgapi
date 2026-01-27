"""
夜轻 Blog
Home: https://blog.yeqing.net/
Docs: https://blog.yeqing.net/acg-api/
"""

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    auto=lambda _: "https://api.yppp.net/api.php",
    horizontal=lambda _: "https://api.yppp.net/pc.php",
    vertical=lambda _: "https://api.yppp.net/pe.php"
)
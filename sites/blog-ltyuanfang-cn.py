"""
远方博客
Home: https://blog.ltyuanfang.cn/

风景图
"""

from imgapi import ImageAPI

api = ImageAPI(
    __name__,
    horizontal=lambda _: "https://tu.ltyuanfang.cn/api/fengjing.php",
)

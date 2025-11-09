import typing as t
import importlib
import os
import asyncio

from fastapi import Request
from loguru import logger as l

import utils as u

_ImgFunc = t.Union[t.Callable[[Request], str], t.Callable[[Request], t.Awaitable[str]]]
_InitFunc = t.Union[t.Callable[[], None], t.Callable[[], t.Awaitable[None]]]


class ImageAPI:
    '''
    图片 API 基类
    '''
    id: str
    '''唯一 id'''
    horizontal: _ImgFunc | None
    '''处理横向图片请求的函数'''
    vertical: _ImgFunc | None
    '''处理竖向图片请求的函数'''
    auto: _ImgFunc | None
    '''处理自适应图片请求的函数'''
    init: _InitFunc | None
    '''在初始化时执行的函数'''

    def __init__(
        self,
        id: str,
        horizontal: _ImgFunc | None = None,
        vertical: _ImgFunc | None = None,
        auto: _ImgFunc | None = None,
        init: _InitFunc | None = None
    ):
        '''
        声明一个图片 API

        :param id: 唯一 id, 直接传入 __name__ 以使用文件名
        :param horizontal: 处理横向图片请求的函数
        :param vertical: 处理竖向图片请求的函数
        :param auto: 处理自适应图片请求的函数
        :param init: 在初始化时执行的函数
        '''
        self.id = id.split('.')[-1]
        self.horizontal = horizontal
        self.vertical = vertical
        self.auto = auto
        self.init = init


class ImgAPIWrapped(ImageAPI):
    horizontal: _ImgFunc
    vertical: _ImgFunc
    auto: _ImgFunc
    init: _InitFunc


class ImgAPIInit:
    allow_h: set[ImgAPIWrapped] = set()
    allow_v: set[ImgAPIWrapped] = set()
    allow_a: set[ImgAPIWrapped] = set()

    async def load_all(self) -> None:
        p_all = u.perf_counter()
        dirlst = os.listdir('sites/')
        sites = 0
        for n in dirlst:
            name, ext = os.path.splitext(n)
            if ext != '.py' or 'example' in name:
                continue

            p = u.perf_counter()
            module = importlib.import_module(f'sites.{name}')
            for attr in dir(module):
                obj = getattr(module, attr)
                if not isinstance(obj, ImageAPI):
                    continue

                await u.call_init_func(obj.init)

                if obj.horizontal:
                    self.allow_h.add(obj)  # type: ignore
                if obj.vertical:
                    self.allow_v.add(obj)  # type: ignore
                if obj.auto:
                    self.allow_a.add(obj)  # type: ignore

                l.debug(f'Init site {name} from sites/{n} took {p()}ms')
                sites += 1

        l.info(f'Init {sites} sites finished in {p_all()}ms.')
        l.info(f'Loaded: {len(self.allow_h)} Horizontal, {len(self.allow_v)} Vertical, {len(self.allow_a)} Auto.')
        l.debug(f'allow_h sites: {[i.id for i in self.allow_h]}')
        l.debug(f'allow_v sites: {[i.id for i in self.allow_v]}')
        l.debug(f'allow_a sites: {[i.id for i in self.allow_a]}')

from pathlib import Path
import time
import os
import typing as t

from user_agents import parse as parse_ua
from user_agents.parsers import UserAgent
from pydantic import BaseModel


class InitOnceChecker:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # l.debug("Creating new ImgAPIInit instance")
        # else:
            # l.debug("Reusing existing ImgAPIInit instance")
        return cls._instance

    def __init__(self):
        if hasattr(self, 'initialized') and self.initialized:
            # l.debug("ImgAPIInit already initialized, skipping")
            self.new_init = False
            return
        self.initialized = True
        self.new_init = True


def perf_counter():
    '''
    获取一个性能计数器, 执行返回函数来结束计时, 并返回保留两位小数的毫秒值
    '''
    start = time.perf_counter()
    return lambda: round((time.perf_counter() - start)*1000, 2)


def get_path(path: str, create_dirs: bool = True, is_dir: bool = False) -> str:
    '''
    相对路径 (基于主程序目录) -> 绝对路径

    :param path: 相对路径
    :param create_dirs: 是否自动创建目录（如果不存在）
    :param is_dir: 目标是否为目录
    :return: 绝对路径
    '''

    full_path = str(Path(__file__).parent.joinpath(path))
    if create_dirs:
        # 自动创建目录
        if is_dir:
            os.makedirs(full_path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path


def cnen(cn: str, en: str):
    return f'{cn}<br/><i>{en}</i>'


def ua(ua_str: str) -> t.Literal['vertical', 'horizontal', 'unknown']:
    ua_result = parse_ua(ua_str)
    if ua_result.is_mobile:
        # Mobile -> Vertical
        return 'vertical'
    elif ua_result.is_pc or ua_result.is_tablet:
        # PC / Tablet -> Horizontal
        return 'horizontal'
    else:
        # Unknown -> Auto
        return 'unknown'


class _UAResult_Browser(BaseModel):
    family: str | None = None
    version: list[int] | None = None
    version_string: str | None = None


class _UAResult_OS(BaseModel):
    family: str | None = None
    version: list[int] | None = None
    version_string: str | None = None


class _UAResult_Device(BaseModel):
    family: str | None = None
    brand: str | None = None
    model: str | None = None


class UAResult(BaseModel):
    browser: _UAResult_Browser
    os: _UAResult_OS
    device: _UAResult_Device

    is_bot: bool
    is_email_client: bool
    is_mobile: bool
    is_pc: bool
    is_tablet: bool
    is_touch_capable: bool

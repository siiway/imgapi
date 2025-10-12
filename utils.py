from logging import Formatter
from pathlib import Path
from datetime import datetime
import time
import os


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

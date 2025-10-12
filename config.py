import typing as t
from json import loads as load_json

from yaml import safe_load
from pydantic import BaseModel

from utils import get_path


class _LoggingConfigModel(BaseModel):
    '''
    日志配置 Model
    '''

    level: t.Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'] = 'INFO'
    '''
    日志等级
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
    '''

    file: str | None = 'running.log'
    '''
    保存日志文件目录 (留空禁用) \n
    如: `running.log`
    '''

    rotating: bool = True
    '''
    是否启用日志轮转
    '''

    rotating_size: float = 1024
    '''
    日志轮转大小 (单位: KB)
    '''

    rotating_count: int = 5
    '''
    日志轮转数量
    '''


class ConfigModel(BaseModel):
    log: _LoggingConfigModel = _LoggingConfigModel()

    enable_docs: bool = True
    '''
    是否启用 /docs (自带文档页面)
    '''

    root_redirect: str = '/docs'
    '''
    控制根目录将重定向到的 url
    '''


try:
    with open(get_path('config.yaml'), 'r', encoding='utf-8') as f:
        file = load_json(safe_load(f))
except:
    file = {}

config = ConfigModel.model_validate(file)

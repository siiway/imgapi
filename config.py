import typing as t

from yaml import safe_load
from pydantic import BaseModel

from utils import get_path
from logger import l


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

    root_redirect: str | None = '/docs'
    '''
    控制根目录将重定向到的 url
    - 如为 None 则返回 json {"hello": "imgapi", "version": "xxx"}
    '''

    fallback_url: str | None = None
    '''
    当所有 site 都失败时重定向到的 url
    - 如为 None 则返回 503 Service Unavailable
    '''


try:
    with open(get_path('config.yaml'), 'r', encoding='utf-8') as f:
        file = safe_load(f)
except Exception as e:
    l.warning(f'Load config.yaml failed: {e}, will use default config')
    file = {}

config = ConfigModel.model_validate(file)
l.info(f'Startup Config: {config}')

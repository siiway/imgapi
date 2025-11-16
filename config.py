import typing as t

from yaml import safe_load
from pydantic import BaseModel, PositiveInt, field_validator

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

    file: str | None = 'logs/{time:YYYY-MM-DD}.log'
    '''
    日志文件保存格式 (for Loguru)
    - 设置为 None 以禁用
    '''

    file_level: t.Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'] | None = 'INFO'
    '''
    单独设置日志文件中的日志等级, 如设置为 None 则使用 level 设置
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
    '''

    rotation: str | int = '1 days'
    '''
    配置 Loguru 的 rotation (轮转周期) 设置
    '''

    retention: str | int = '3 days'
    '''
    配置 Loguru 的 retention (轮转保留) 设置
    '''

    @field_validator('level', 'file_level', mode='before')
    def normalize_level(cls, v):
        if v is None:
            return v
        if not isinstance(v, str):
            raise ValueError(f'Invaild log level: {v}')
        upper = v.strip().upper()
        valid = {'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'}
        if upper not in valid:
            raise ValueError(f'Invaild log level: {v}')
        return upper

class _FallbackConfigModel(BaseModel):
    horizontal: str | None = None
    '''
    横向图片 url
    '''
    vertical: str | None = None
    '''
    竖向图片 url
    '''
    unknown: str | None = None
    '''
    其他图片 url
    '''

class ConfigModel(BaseModel):
    log: _LoggingConfigModel = _LoggingConfigModel()
    '''
    日志相关配置
    '''

    fallback: _FallbackConfigModel = _FallbackConfigModel()
    '''
    当所有 site 都失败时重定向到的 url
    - 如为 None 则返回 503 Service Unavailable
    '''

    node: str = 'default'
    '''
    节点名称, 用于在多节点部署 (如 CF Tunnel) 的情况下区分响应请求的节点
    '''

    host: str = '0.0.0.0'
    '''
    服务监听地址 (仅在直接启动 main.py 时有效)
    '''

    port: PositiveInt = 9333
    '''
    服务监听端口 (仅在直接启动 main.py 时有效)
    '''

    workers: PositiveInt = 2
    '''
    服务 Worker 数 (仅在直接启动 main.py 时有效)
    '''

    enable_docs: bool = True
    '''
    是否启用 /docs (自带文档页面)
    '''

    root_redirect: str | None = '/docs'
    '''
    控制根目录将重定向到的 url
    - 如为 None 则返回 json {"hello": "imgapi", "version": "xxx"}
    '''

try:
    with open(get_path('config.yaml'), 'r', encoding='utf-8') as f:
        file = safe_load(f)
    load_config_failed = None
except Exception as e:
    load_config_failed = e
    file = {}

config = ConfigModel.model_validate(file)

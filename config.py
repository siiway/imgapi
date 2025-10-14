import typing as t

from yaml import safe_load
from pydantic import BaseModel, PositiveInt

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

    file: bool = True
    '''
    是否保存日志文件
    - 存储在 logs/YYYY-MM-DD.log
    '''

    rotation: str = '1 days'
    '''
    配置 Loguru 的 rotation (轮转周期) 设置
    '''

    retention: str = '3 days'
    '''
    配置 Loguru 的 retention (轮转保留) 设置
    '''


class ConfigModel(BaseModel):
    log: _LoggingConfigModel = _LoggingConfigModel()

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

    workers: PositiveInt = 3
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

    fallback_url: str | None = None
    '''
    当所有 site 都失败时重定向到的 url
    - 如为 None 则返回 503 Service Unavailable
    '''


try:
    with open(get_path('config.yaml'), 'r', encoding='utf-8') as f:
        file = safe_load(f)
    load_config_failed = None
except Exception as e:
    load_config_failed = e
    file = {}

config = ConfigModel.model_validate(file)

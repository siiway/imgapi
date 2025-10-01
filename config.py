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

    host: str = '0.0.0.0'
    '''
    服务监听地址 (只在直接启动 main.py 时有效)
    '''

    port: PositiveInt = 9333
    '''
    服务端口 (只在直接启动 main.py 时有效)
    '''

    debug: bool = False
    '''
    是否开启调试模式 (只在直接启动 main.py 时有效)
    '''

    


try:
    with open(get_path('config.yaml'), 'r', encoding='utf-8') as f:
        file = safe_load(f)
except:
    file = {}

config = ConfigModel.model_validate(file)

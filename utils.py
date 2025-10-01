from logging import Formatter
from pathlib import Path
from datetime import datetime
import os


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


class CustomFormatter(Formatter):
    '''
    自定义的 logging formatter
    '''
    # symbols = {
    #     'DEBUG': '⚙️ ',
    #     'INFO': 'ℹ️ ',
    #     'WARNING': '⚠️ ',
    #     'ERROR': '❌',
    #     'CRITICAL': '💥'
    # }
    replaces = {
        'DEBUG': f'[DEBUG]',
        'INFO': f'[INFO] ',
        'WARNING': f'[WARN] ',
        'ERROR': f'[ERROR]',
        'CRITICAL': f'[CRIT] '
    }
    # replaces_colorful = {
    #     'DEBUG': f'{Fore.BLUE}[DEBUG]{Style.RESET_ALL}',
    #     'INFO': f'{Fore.GREEN}[INFO]{Style.RESET_ALL} ',
    #     'WARNING': f'{Fore.YELLOW}[WARN]{Style.RESET_ALL} ',
    #     'ERROR': f'{Fore.RED}[ERROR]{Style.RESET_ALL}',
    #     'CRITICAL': f'{Fore.MAGENTA}[CRIT]{Style.RESET_ALL} '
    # }
    # default_symbol = '📢'
    # colorful: bool

    # def __init__(self, colorful: bool = True):
    # super().__init__()
    # if colorful:
    #     self.replaces = self.replaces_colorful
    # else:
    #     self.replaces = self.replaces_nocolor
    #     self.symbols = {}
    #     self.default_symbol = ''

    def format(self, record):
        timestamp = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')  # 格式化时间
        # symbol = f' {self.symbols.get(record.levelname, self.default_symbol)}'  # 表情符号
        level = self.replaces.get(record.levelname, f'[{record.levelname}]')  # 日志等级
        file = os.path.relpath(record.pathname)  # 源文件名
        line = record.lineno  # 文件行号

        message = super().format(record)  # 日志内容
        # formatted_message = f"{timestamp}{symbol} {level} | {file}:{line} | {message}"
        formatted_message = f"{timestamp} {level} | {file}:{line} | {message}"
        return formatted_message

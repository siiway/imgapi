import json
import os
import sys
from colorama import Fore, Style


# ---
# Get paths

def get_basepath(self):
    '''
    获取 base path (main.py 所在目录)
    '''
    main_py = sys.argv[0]
    return os.path.dirname(main_py)


def get_datapath(path):
    '''
    将相对路径的数据目录改为绝对路径
    @param path: 相对路径
    '''
    return os.path.join(self.get_basepath(), path)

# ---
# Logging


'''
info 信息
warning 警告
error 错误
debug 调试 -> Only show when `env_debug == True`

@param noret: 是否在输出最后取消换行

+s -> 多行输出 (每行为一参数)
'''


def info(msg, noret=False):
    if noret:
        print(f'{Fore.GREEN}[I]{Style.RESET_ALL} {msg}', end='')
    else:
        print(f'{Fore.GREEN}[I]{Style.RESET_ALL} {msg}')


def warning(msg, noret=False):
    if noret:
        print(f'{Fore.YELLOW}[W]{Style.RESET_ALL} {msg}', end='')
    else:
        print(f'{Fore.YELLOW}[W]{Style.RESET_ALL} {msg}')


def error(msg, noret=False):
    if noret:
        print(f'{Fore.RED}[E]{Style.RESET_ALL} {msg}', end='')
    else:
        print(f'{Fore.RED}[E]{Style.RESET_ALL} {msg}')


def debug(msg, noret=False):
    if noret:
        print(f'{Fore.BLUE}[D]{Style.RESET_ALL} {msg}', end='')
    else:
        print(f'{Fore.BLUE}[D]{Style.RESET_ALL} {msg}')

    # ↑单行 / ↓多行


def infos(*msgs, noret=False):
    for n in msgs:
        if n == msgs[-1]:
            if noret:
                print(f'{Fore.GREEN}[I]{Style.RESET_ALL} {n}', end='')
            else:
                print(f'{Fore.GREEN}[I]{Style.RESET_ALL} {n}')
        else:
            print(f'{Fore.GREEN}[I]{Style.RESET_ALL} {n}')


def warnings(*msgs, noret=False):
    for n in msgs:
        if n == msgs[-1]:
            if noret:
                print(f'{Fore.YELLOW}[W]{Style.RESET_ALL} {n}', end='')
            else:
                print(f'{Fore.YELLOW}[W]{Style.RESET_ALL} {n}')
        else:
            print(f'{Fore.YELLOW}[W]{Style.RESET_ALL} {n}')


def errors(*msgs, noret=False):
    for n in msgs:
        if n == msgs[-1]:
            if noret:
                print(f'{Fore.RED}[E]{Style.RESET_ALL} {n}', end='')
            else:
                print(f'{Fore.RED}[E]{Style.RESET_ALL} {n}')
        else:
            print(f'{Fore.RED}[E]{Style.RESET_ALL} {n}')


def debugs(*msgs, noret=False):
    for n in msgs:
        if n == msgs[-1]:
            if noret:
                print(f'{Fore.BLUE}[D]{Style.RESET_ALL} {n}', end='')
            else:
                print(f'{Fore.BLUE}[D]{Style.RESET_ALL} {n}')
        else:
            print(f'{Fore.BLUE}[D]{Style.RESET_ALL} {n}')

# ---
# Format


def format_dict(dic):
    '''
    列表 -> 格式化 json
    @param dic: 列表
    '''
    return json.dumps(dic, indent=4, ensure_ascii=False, sort_keys=False, separators=(', ', ': '))


def remove_json(lst):
    '''
    移除列表中每项末尾的 `.json`
    @param lst: 列表
    '''
    lst_after = []
    for i in lst:
        lst_after += [os.path.splitext(i)[0]]
    return lst_after

# ---
# Load / File (dir) option


def load_json(json_name):
    '''
    加载 json 文件
    '''
    try:
        with open(json_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.decoder.JSONDecodeError as err:
        self.error(f'Load json file "{json_name}" Failed! Please check the json format!')
        raise


def read_dir(dirpath):
    '''
    遍历文件夹
    @param dirpath: 文件夹路径
    '''
    if not os.path.exists(dirpath):
        raise NotADirectoryError(f'{dirpath} not exist.')
    indir_list = []
    for filename in os.listdir(dirpath):
        indir_list += [filename]
    return indir_list

# ---
# Terminal option


backlinestr = '\033[F\033[K'  # 退行


def backline(num=1):
    '''
    退行
    @param num: 行数
    '''
    for i in range(num + 1):
        print(self.backlinestr, end='')
    # print()


def prints(*args):
    '''
    方便输出多行文本
    '''
    for n in args:
        print(n)

# imgapi

Siiway 图片集合 API

> 正在开发中

按原则来说，本站 API:
- **不提供 R18 类图片**
- 不提供动图

## 整理

请见 [Here](./sites.md)

介绍了我们 API 库里收集的所有 API

## API

地址: Nope

会在我们的 API 库里随机选择返回

~~有 `Json` 和 `图片` 两种调用方式~~

只有图片返回，因为 json 字段名各站不同

### 部署

0. Clone 本仓库

```shell
git clone https://github.com/wyf01239/imgapi.git
```

1. 安装依赖

```shell
./install.sh
# Windows:
install.bat
```

2. 配置应用

编辑 `config.py`:

```py
host = '0.0.0.0' # 监听地址，`0.0.0.0` 代表所有
port = 9333 # 监听端口
debug = False # (二次开发建议启用) 控制 Flask 的 debug 选项，打开后可以提供脚本热重载 (ps: 没写好就保存容易使其因语法问题崩溃)
```

3. 启动程序

```shell
python3 server.py
# `python3` 自行替换为你的 Python 程序
```

> 建议 Python 版本: `3.10+`
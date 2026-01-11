# ImgAPI

一个集合了全网背景图片 API 的随机跳转 API

按原则来说，本站 API:
- **不提供 R18 图片**
- **不提供动图**

## TODOs

- [x] sites 迁移
- [x] 补全配置文档
- [x] 设置节点名称
- [x] 上个版本的 api 兼容
- [x] UA 测试页面
- [x] public 文件夹
- [x] fallback 设置
- [ ] *Site Healthcheck* - pr welcome
- [ ] *预加载图片地址* - pr welcome

## 整理

请见 [Here](./sites.md)

介绍了我们 API 库里收集的所有 API

## API

中国大陆区域:

- `imgapi.siiway.top`
- `i.wss.moe`

海外区域:

- `imgapi-origin.siiway.top`
- `io.wss.moe`

> 建议自行部署，只需有 Python3 环境 (建议 uv) 即可

| 接口       | 信息                               |
| ---------- | ---------------------------------- |
| `/`        | 跳转到设置的 URL 或者返回 API 信息 |
| `/image`   | 自动                               |
| `/image/h` | 横向图片                           |
| `/image/v` | 竖向图片                           |
| `/ua`      | UA 测试结果                        |

> [!TIP]
> 更详细的 API 返回信息见: **[Swagger](https://imgapi.siiway.top/docs)** / **[Redoc](https://imgapi.siiway.top/redoc)**

> [!TIP]
> 几种图片类型的解释: <br/>
> 1. `/image`: 由本项目服务器使用 User-Agent 判断设备类型，如无法判断则降级至由三方 API 处理 - **推荐使用** <br/>
> 2. `/image/h`: 横向 *(水平, Horizontal)*, 适用于电脑/平板 <br/>
> 3. `/image/v`: 竖向 *(垂直, Vertical)*, 适用于手机

## 部署

> [!IMPORTANT]
> 要求 Python 版本: **>= 3.10**

1. Clone 本仓库

```bash
git clone https://github.com/siiway/imgapi.git
```

2. 安装依赖

```bash
uv sync
# 如果没有 uv:
# pip install -r requirements.txt
```

<!-- uv export > requirements.txt -->

3. (可选) 配置服务

创建 `config.yaml`:

```yaml
# 节点名称, 用于在多节点部署 (如 CF Tunnel) 的情况下区分响应请求的节点
node: default
# 服务监听地址 (仅在直接启动 main.py 时有效)
host: '0.0.0.0'
# 服务监听端口 (仅在直接启动 main.py 时有效)
port: 9333
# 服务 Worker 数 (仅在直接启动 main.py 时有效)
workers: 2
# 是否启用 /docs (自带文档页面)
enable_docs: true
# 控制根目录将重定向到的 url
# 如为 null 则返回 json {"hello": "imgapi", "version": "xxx"}
root_redirect: /docs
# 当所有 site 都失败时重定向到的 url
# 如为 null 则返回 503 Service Unavailable
fallback:
  # 横向图片 url
  horizontal: null
  # 竖向图片 url
  vertical: null
  # 其他图片 url
  unknown: null
# 日志相关配置
log:
  # 日志等级 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  level: INFO
  # 日志文件保存格式 (for Loguru)
  # 设置为 None 以禁用
  file: 'logs/{time:YYYY-MM-DD}.log'
  # 单独设置日志文件中的日志等级
  # 如设置为 null 则使用 level 设置
  file_level: DEBUG
  # 配置 Loguru 的 rotation (轮转周期) 设置
  rotation: 1 days
  # 配置 Loguru 的 retention (轮转保留) 设置
  retention: 3 days
```

4. 启动程序

直接启动 (使用配置中的 host & port & workers, **推荐**):

```bash
uv run main.py
# or python3 main.py
```

使用 cli 启动 (另外指定 host & port):

```bash
uv run fastapi run --host 0.0.0.0 --port 9333
# or fastapi run --host 0.0.0.0 --port 9333
```

## 声明

本项目仅提供了随机的 302 跳转 api，并未 存储/代理 任何图片资源，其版权归原作者所有，与本项目无**任何**关联.

如对此项目有建议/问题，可 [Issue](https://github.com/siiway/imgapi/issue/new) / [Contact](https://wyf9.top/t/c)

*部分 API 来源：https://blog.jixiaob.cn/?post=93*

(c) 2026 SiiWay Team. Under MIT License.

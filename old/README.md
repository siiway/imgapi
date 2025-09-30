# imgapi

一个集合全网图片 api 的 api *~~(实际上就是随机选择一个跳转)~~*

按原则来说，本站 API:
- **不提供 R18 类图片**
- **不提供动图**

## 整理

请见 [Here](./sites.md)

介绍了我们 API 库里收集的所有 API

## API

公共服务: [imgapi.siiway.top](https://imgapi.siiway.top/about)

> 建议自行部署，只需有 Python3 环境即可

| 接口       | 信息          |
| ---------- | ------------- |
| `/`        | 跳转到本 repo |
| `/image`   | 自动          |
| `/img`     | -             |
| `/image/s` | 自适应图片    |
| `/img/s`   | -             |
| `/image/h` | 横向图片      |
| `/img/h`   | -             |
| `/image/v` | 竖向图片      |
| `/img/v`   | -             |

> [!TIP]
> 几种图片类型的解释: <br/>
> 1. `a`: 自动 *(Auto)*, 由本项目服务器使用 User-Agent 判断设备类型，如无法判断则降级至 `s` - **推荐使用** <br/>
> 2. `s`: 自适应 *(Self)*, 由第三方服务自行判断设备类型 <br/>
> 3. `h`: 横向 *(水平, Horizontal)*, 适用于电脑/平板 <br/>
> 4. `v`: 竖向 *(垂直, Vertical)*, 适用于手机

### 部署

1. Clone 本仓库

```shell
git clone https://github.com/siiway/imgapi.git
```

2. 安装依赖

```shell
cd imgapi
pip install -r requirements.txt
```

> **推荐使用 uv 管理依赖:**

```shell
cd imgapi
uv sync
```

3. (可选) 配置服务

创建 `config.json`，内容如下

```jsonc
{
    "host": "0.0.0.0", // 监听地址，`0.0.0.0` 代表所有 (如需监听 ipv6 则改为 `::`)
    "port": 9333, // 监听端口
    "debug": false // (二次开发建议启用) 启用 Flask 热重载
}
```

4. 启动程序

```shell
python3 main.py
# 或者 uv run main.py (不需要激活 venv)
```

> 建议 Python 版本: **3.11+**

## 声明

本项目仅提供了随机的 302 跳转 api，并未 存储/代理 任何图片资源，其版权归原作者所有，与本项目无**任何**关联.

如对此项目有建议/问题，可 [Issue](https://github.com/siiway/imgapi/issue/new) / [Contact](https://wyf9.top/t/c)

*部分 API 来源：https://blog.jixiaob.cn/?post=93*

(c) 2025 SiiWay Team. Under MIT License.

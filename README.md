# ImgAPI

一个集合了全网背景图片 API 的随机跳转 API

按原则来说，本站 API:
- **不提供 R18 类图片**
- **不提供动图**

## TODO

- [ ] sites 迁移
- [ ] 补全配置文档
- [ ] 调用统计

## 整理

请见 [Here](./sites.md)

介绍了我们 API 库里收集的所有 API

## API

公共服务: `imgapi.siiway.top`

> 建议自行部署，只需有 Python3 环境 (建议 uv) 即可

| 接口       | 信息                               |
| ---------- | ---------------------------------- |
| `/`        | 跳转到设置的 URL 或者返回 API 信息 |
| `/image`   | 自动                               |
| `/image/a` | 自适应图片                         |
| `/image/h` | 横向图片                           |
| `/image/v` | 竖向图片                           |

> [!TIP]
> 几种图片类型的解释: <br/>
> 1. `/image`: 由本项目服务器使用 User-Agent 判断设备类型，如无法判断则降级至 `s` - **推荐使用** <br/>
> 2. `/image/a`: 自动 *(Auto)*, 由第三方服务自行判断设备类型 <br/>
> 3. `/image/h`: 横向 *(水平, Horizontal)*, 适用于电脑/平板 <br/>
> 4. `/image/v`: 竖向 *(垂直, Vertical)*, 适用于手机

## 部署

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

```

4. 启动程序

```bash
uv run fastapi run --host 0.0.0.0 --port 9333
```

## 声明

本项目仅提供了随机的 302 跳转 api，并未 存储/代理 任何图片资源，其版权归原作者所有，与本项目无**任何**关联.

如对此项目有建议/问题，可 [Issue](https://github.com/siiway/imgapi/issue/new) / [Contact](https://wyf9.top/t/c)

*部分 API 来源：https://blog.jixiaob.cn/?post=93*

(c) 2025 SiiWay Team. Under MIT License.

# imgapi

一个可以集合全网图片 api 的 api

按原则来说，本站 API:
- **不提供 R18 类图片**
- 不提供动图

## 整理

请见 [Here](./sites.md)

介绍了我们 API 库里收集的所有 API

## API

公共服务: https://imgapi.siiway.top

> 使用 `Serv00 免费服务` + `Cloudflare Tunnel` 部署，不作访问限制（为账号安全请节省使用)

> 建议自行部署，只需有 Python3 环境即可

| 接口       | 信息                 |
| ---------- | -------------------- |
| `/`        | 跳转到本 repo        |
| `/image`   | 跳转到随机自适应图片 |
| `/image/a` | 自适应图片           |
| `/img/a`   | -                    |
| `/image/h` | 横向图片             |
| `/img/h`   | -                    |
| `/image/v` | 竖向图片             |
| `/img/v`   | -                    |

<!-- 会在我们的 API 库里随机选择返回
~~有 `Json` 和 `图片` 两种调用方式~~
只有图片返回，因为 json 字段名各站不同 -->

### 部署

1. Clone 本仓库

```shell
git clone https://github.com/siiway/imgapi.git
```

2. 安装依赖

```shell
./install.sh
# Windows:
install.bat
```

3. 配置服务

编辑 `config.py`:

```py
host = '0.0.0.0' # 监听地址，`0.0.0.0` 代表所有
port = 9333 # 监听端口
debug = False # (二次开发建议启用) 控制 Flask 的 debug 选项，打开后可以提供脚本热重载 (ps: 没写好就保存容易使其因语法问题崩溃)
```

4. 启动程序

```shell
python3 server.py
# `python3` 自行替换为你的 Python 程序
```

> 建议 Python 版本: `3.10+`

## 声明

本项目仅提供了随机的 302 跳转 api，并未 存储/代理 任何图片资源，其版权归原作者所有，与本项目无关.

如对此项目有建议/问题，可 [Issue](https://github.com/siiway/imgapi/issue/new)，或 [点此](https://wyf9.top/#/contact) 跳转联系方式.

部分 API 来源：https://blog.jixiaob.cn/?post=93

## TODO

```md
> 从哪里的 alist 配置示例中扒的
- [x] (重复) 樱花：https://www.dmoe.cc/
- [√] 夏沫：https://cdn.seovx.com/
- [ ] (undone) 搏天：https://api.btstu.cn/doc/sjbz.php
- [ ] 姬长信：https://github.com/insoxin/API
- [ ] 小歪：https://api.ixiaowai.cn/
- [ ] 保罗：https://api.paugram.com/
- [ ] 墨天逸：https://api.mtyqx.cn/
- [ ] 岁月小筑：https://img.xjh.me/
- [ ] 东方Project：https://img.paulzzh.com/
```
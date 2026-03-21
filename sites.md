# Sites

本页收集各种图片 API 站点

> [!TIP]
> 本项目收集的每个 API 都在 `sites/` 目录下作为一个独立的文件 (文件名即为下面 `id`)，由主程序遍历导入，并创建路由 _(文件名去 `.py`)_

## 栗次元 API

id: `t-alcy-cc`

主站: <https://t.alcy.cc/>

食用方法 (作者博客): <https://www.alcy.cc/archives/sui-ji-er-ci-yuan-tu-pian-api>

API 发布页: <https://t.mwm.moe/>

有两种调用方法: **图片**，**json**

> 类别请见 [主站](https://t.alcy.cc/)

### 图片调用

```url
https://t.alcy.cc/<类别>
```

### json 调用

```url
https://t.alcy.cc/<类别>?json
```

返回示例:

```jsonc
{
  "code": 200, // http status code
  "url": "https:\/\/tc.alcy.cc\/i\/2024\/04\/21\/662416447bef8.webp", // 图片 url
  "width": 1200, // 宽
  "height": 675, // 高
}
```

## 98情缘 API

id: `www-98qy-com`

文档: <https://www.98qy.com/sjbz/>

Get 方式请求固定地址: <https://www.98qy.com/sjbz/api.php> , 返回 **图片** 或 **Json**

> 请求参数详见 [文档](https://www.98qy.com/sjbz/)

## Lolicon API

- ~~Maybe~~ **R18**

随机涩图 _(pixiv)_ API

v2: <https://api.lolicon.app/setu/v2> (GET / POST)

返回格式仅有 **Json** _(包含图片链接)_，但有大量自定义选项

详见文档: <https://api.lolicon.app/#/setu>

## 岁月小筑动漫壁纸

地址: <https://cloud.qqshabi.cn/api/images/api.php>

不需要参数，直接返回图片 _(横向?)_

文档: <https://cloud.qqshabi.cn/apidetail/33.html>

> 原版 API: <https://img.xjh.me/random_img.php> , 注意: 返回的是带百度统计的网页，不是图片

## 樱花随机二次元图片 API

id: `www-dmoe-cc`

接口地址: <https://www.dmoe.cc/random.php>

文档: <https://www.dmoe.cc/>

有两种调用方式:

- 图片: <https://www.dmoe.cc/random.php> _(ps: 直接访问会下载)_
- Json: <https://www.dmoe.cc/random.php?return=json>

Json 返回:

```jsonc
{
  "code": "200", // http status code
  "imgurl": "https:\/\/ws1.sinaimg.cn\/large\/0072Vf1pgy1foxkfy08umj31kw0w0nng.jpg", // 图片 url
  "width": "2048", // 宽
  "height": "1152", // 高
}
```

> _仅横图?_

## Unsplash

一个国外的高质量开放照片集 _(三次元)_ 平台，有丰富的 API，支持搜索

官网: <https://unsplash.com/developers>

> 需要注册才可使用

## 零七生活 API

文档: <https://api.oick.cn/doc/random>

接口地址: <https://api.oick.cn/api/random> (GET)

参数:

- `?type=pc`: 电脑壁纸 (横向)
- `?type=pe`: 手机壁纸 (竖向)

## 赫萝随机图片 API

id: `api-horosama-com`

文档: <https://api.horosama.com/>

接口: <https://api.horosama.com/random.php>

常用有两个参数 _(粗体为默认)_:

- `type`: 图片类型 (**`pc`-横**, `mobile`-竖, `profile`-头像)
- `format`: 返回格式 (**`image`**, `json`)

json 返回示例:

```jsonc
{
  "code": "200", // 状态码
  "url": "https:\/\/www.horosama.com\/api\/image_all\/anime\/1080p\/pc\/efA6f53Bc7A635089D125a90f4d2081F.jpg",
  // 图片地址
  "width": "1920", // 图片宽度
  "height": "1080", // 图片高度
}
```

## 夏沫博客 API

id: `cdn-seovx-com`

文档: <https://cdn.seovx.com/>

有三个 302 接口 (all GET)：

- 美图: <https://cdn.seovx.com/?mom=302>
- 二次元： <https://cdn.seovx.com/d/?mom=302> √
- 古风： <https://cdn.seovx.com/ha/?mom=302>

## 搏天 API

id: `api-btstu-cn`

文档: <https://api.btstu.cn/doc/sjbz.php>

API: <https://api.btstu.cn/sjbz/api.php>

请求参数:

- `method`: 图片长宽比 (`mobile`, `pc`, **`zsy`**)
- `lx`: 分类 (`meizi`, `dongman`, `fengjing`. **`suiji`**)
- `format`: 格式 (`json`, **`images`**)

json 返回示例:

```jsonc
{
  "code": "200", // 状态码
  "imgurl": "https:\/\/tva4.sinaimg.cn\/large\/9bd9b167gy1g2qkr95hylj21hc0u01kx.jpg", // 图片地址
  "width": "1920", // 图片宽度
  "height": "1080", // 图片高度
}
```

## 保罗 API

id: `api-paugram-com`

文档: <https://api.paugram.com/help/wallpaper>

API: <https://api.paugram.com/wallpaper/>

请求参数:

- `source`: 图片源 (**`sm`**, `cp`, `sina`, `paul`, `gh`, `jsd`) **_存疑_**
- `category`: **[施工中]** 分类 (`us`, `jp`, `cn`, `1`, `2`, `3`) **_存疑_**

示例: `https://api.paugram.com/wallpaper/?source=sm`

## 墨天逸 API

id: `api-mtyqx-cn`

文档: <https://api.mtyqx.cn/>

API: <https://api.mtyqx.cn/api/random.php>

## Paulzzh API

id: `img-paulzzh-com`

东方 Project 随机图片 API

文档: <https://img.paulzzh.com/>

API: <https://img.paulzzh.com/touhou/random>

请求参数:

- `type`: 返回类型 (**`302`**, `json`)
- `site`: 源站点 (**`konachan`**, `yandere`, `all`)
- `size`: 图片尺寸 (**`pc`**, `wap`, `all`)
- `tag`: 标签 _(beta)_ - 见 [Here](https://img.paulzzh.com/touhou/random_tags)

## xiaoyuan的牛肉随机图API

id: `img-xiaoyuan151-com`

文档: `{Null}`

API: <https://img.xiaoyuan151.com/neuro>

> 自动判断 UA

## Imlazy API

id: `api-imlazy-ink`

文档: <https://api.imlazy.ink/#/img>

API:

- 横向: <https://api.imlazy.ink/img>
- 竖向: <https://api.imlazy.ink/img-phone>

> [!TIP]
> 也可使用 `s7.imlazy.ink`

## 2x🌲🌲 的随机图 API

id: `c-p-2x-nz`

~~Blog Post: <https://2x.nz/posts/acg-randompic-api/>~~

Source Repo: https://github.com/afoim/choice_randompic

API:

- 横向: <https://c-p.2x.nz/h>
- 竖向: <https://c-p.2x.nz/v>
- 图源: <https://2x.nz/gallery/>

## baigei的随机图api

id: `baigei-cc`

Blog Post: <https://baigei.cc/index.php/archives/28/>

API:

- 自动 (芙宁娜): <https://furina.baigei.cc/index.php>
- 横向 (芙宁娜): <https://furina.baigei.cc/pc.php>
- 竖向 (芙宁娜): <https://furina.baigei.cc/phone.php>
- 自动 (昔涟): <https://philia093.baigei.cc/index.php>
- 横向 (昔涟): <https://philia093.baigei.cc/pc.php>
- 竖向 (昔涟): <https://philia093.baigei.cc/phone.php>

## 远方博客

id: `blog-ltyuanfang-cn`

Blog Post: <https://blog.ltyuanfang.cn/241.html>

API: <https://tu.ltyuanfang.cn/api/fengjing.php>

## 夜轻 Blog

id: `blog-yeqing-net`

文档: <https://blog.yeqing.net/acg-api/>

API:

- 自动: <https://api.yppp.net/api.php>
- 横向: <https://api.yppp.net/pc.php>
- 竖向: <https://api.yppp.net/pe.php>

## YM-API 与末API

id: `img-api-yumo-cc`

文档: <https://img-api.yumo.cc/>

API:

- Muse Dash: <https://img-api.yumo.cc/api/muse-dash-bg/>
- 和泉纱雾: <https://img-api.yumo.cc/api/hqsw-bg/>
- 心跳文学社: <https://img-api.yumo.cc/api/ddlc-bg/>

## 图样跑酷

id: `img-run`

主页: <https://img.run/>

API: <https://bing.img.run/rand.php>

## 明月浩空网

id: `myhkw-cn`

主页: <https://myhkw.cn/>

API:

- Bing 每日壁纸: <https://myhkw.cn/open/img/bing>
- 动态莫哈维昼夜图片: <https://myhkw.cn/open/img/mojave>

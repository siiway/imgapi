# Sites

本页收集各种图片 API 站点


> `id` 是什么? 简单来说就是 `sites/` 目录下相应的文件名

> 本项目收集的每个 API 都在 `sites/` 目录下作为一个独立的文件，由主程序遍历导入，并创建路由 *(文件名去 `.py`)*

> [!TIP]
> 如果没有 `id` 呢? 代表未收入项目随机 API 的列表中

## 栗次元 API

id: `liciyuan`

主站: https://t.alcy.cc/

食用方法 (作者博客): https://www.alcy.cc/archives/sui-ji-er-ci-yuan-tu-pian-api

API 发布页: https://t.mwm.moe/

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
    "height": 675 // 高
}
```

## 98情缘 API

id: `98qy`

文档: https://www.98qy.com/sjbz/

Get 方式请求固定地址: https://www.98qy.com/sjbz/api.php , 返回 **图片** 或 **Json**

> 请求参数详见 [文档](https://www.98qy.com/sjbz/)

## Lolicon API

- Maybe **R18**

随机涩图 *(pixiv)* API

v2: https://api.lolicon.app/setu/v2 (GET / POST)

返回格式仅有 **Json** *(包含图片链接)*，但有大量自定义选项

详见文档: https://api.lolicon.app/#/setu

## 岁月小筑动漫壁纸

id: `xiaozhu`

地址: https://cloud.qqshabi.cn/api/images/api.php

不需要参数，直接返回图片 *(横向?)*

文档: https://cloud.qqshabi.cn/apidetail/33.html

> 原版 API: https://img.xjh.me/random_img.php , 注意: 返回的是带百度统计的网页，不是图片

## 樱花随机二次元图片 API

id: `yinghua`

接口地址: https://www.dmoe.cc/random.php

文档: https://www.dmoe.cc/

有两种调用方式:

- 图片: https://www.dmoe.cc/random.php *(ps: 直接访问会下载)*
- Json: https://www.dmoe.cc/random.php?return=json

Json 返回:

```jsonc
{
    "code": "200", // http status code
    "imgurl": "https:\/\/ws1.sinaimg.cn\/large\/0072Vf1pgy1foxkfy08umj31kw0w0nng.jpg", // 图片 url
    "width": "2048", // 宽
    "height": "1152" // 高
}
```

> *仅横图?*

## 韩小韩 API (Bing, 风景, 二次元)

id: `hanxiaohan`

- Bing:
  - 接口: https://api.vvhan.com/api/bing
  - 文档: https://api.vvhan.com/article/bing.html
- 风景:
  - 接口: https://api.vvhan.com/api/wallpaper/views
  - 文档: https://api.vvhan.com/article/views.html
- 二次元:
  - 接口: https://api.vvhan.com/api/wallpaper/acg
  - 文档: https://api.vvhan.com/article/acg.html

支持两种格式 (图片 / json)，默认为返回图片，在接口后加参 `?type=json` 返回 json

1. Bing json 返回:

```jsonc
{
    "success": true, // 是否成功
    "data": {
        "id": 1644,
        "date": 20240823,
        "title": "帕侬蓝寺，武里南府，泰国 (© Banjongseal324/Getty Images)", // 标题
        "url": "https://cn.bing.com/th?id=OHR.PrasatPhanom_ZH-CN0445884858_UHD.jpg&w=4096" // 图片地址
    }
}
```

2. 风景 / 二次元 json 返回:

```jsonc
{
    "success": true, // 是否成功
    "type": "风景", // 类型
    "url": "https://api-storage.4ce.cn/v1/a1cd42b2bd007599ae70bc580061a2d8.webp" // 图片地址
}
```

## Unsplash

一个国外的高质量开放照片集 *(三次元)* 平台，有丰富的 API，支持搜索

官网: https://unsplash.com/developers

> 需要注册才可使用

## 零七生活 API

id: `lingqi`

文档: https://api.oick.cn/doc/random

接口地址: https://api.oick.cn/api/random (GET)

参数:

- `?type=pc`: 电脑壁纸 (横向)
- `?type=pe`: 手机壁纸 (竖向)

## 赫萝随机图片 API

id: `horosama`

文档: https://api.horosama.com/

接口: https://api.horosama.com/random.php

常用有两个参数 *(粗体为默认)*:

- `type`: 图片类型 (**`pc`-横**, `mobile`-竖, `profile`-头像)
- `format`: 返回格式 (**`image`**, `json`)

json 返回示例:

```json
{
    "code": "200", // 状态码
    "url": "https:\/\/www.horosama.com\/api\/image_all\/anime\/1080p\/pc\/efA6f53Bc7A635089D125a90f4d2081F.jpg",
    // 图片地址
    "width": "1920", // 图片宽度
    "height": "1080" // 图片高度
}
```
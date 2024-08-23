# Sites

本页收集了网络上的图片 API 站点，以及调用方法等


> `id` 是什么? 简单来说就是 `sites/` 目录下相应的文件名

> 本项目收集的每个 API 都在 `sites/` 目录下作为一个独立的文件，由主程序遍历导入，并创建路由 *(文件名去 `.py`)*

> [!TIP]
> 如果没有 `id` 呢? 代表未收入我们随机 API 的列表中

## 栗次元 API

id: `liciyuan`

主站: https://t.alcy.cc/

食用方法 (作者博客): https://www.alcy.cc/archives/sui-ji-er-ci-yuan-tu-pian-api

API 发布页: https://t.mwm.moe/

有两种调用方法: **图片**，**json**

> [!NOTE]
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


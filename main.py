import logging
from random import choice
from sys import stderr, argv

from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html
from pydantic import BaseModel
from user_agents import parse as parse_ua
from loguru import logger as l
from uvicorn import run

from config import config as c, load_config_failed
import utils as u
from utils import cnen as ce
from imgapi import ImgAPIInit

VERSION = '2025.10.17'

# region init

# init logger
l.remove()

l.add(
    stderr,
    level=c.log.level,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>"
)

if c.log.file:
    l.add(
        'logs/{time:YYYY-MM-DD}.log',
        level=c.log.level,
        rotation=c.log.rotation,
        retention=c.log.retention
    )


class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = l.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())


logging.getLogger('uvicorn').handlers.clear()
logging.getLogger().handlers = [InterceptHandler()]
logging.getLogger().setLevel(c.log.level)
logging.getLogger('watchfiles').level = logging.WARNING  # set watchfiles logger level

if load_config_failed:
    l.warning(f'Load config.yaml failed: {load_config_failed}, will use default config')


# endregion init

# region app

l.info(f'Startup Config: {c}')
l.info(f'Node: {c.node}')

l.info(f'{'='*25} Application Startup {'='*25}')

l.info(f'ImgAPI v{VERSION} by SiiWay Team')
l.info('Under MIT License')
l.info('GitHub: https://github.com/siiway/imgapi')

app = FastAPI(
    title=f'ImgAPI - {c.node}',
    description='一个简单的随机背景图 API, 基于 FastAPI | A simple random background image API based on FastAPI | https://github.com/siiway/imgapi',
    version=VERSION,
    docs_url=None,
    redoc_url=None
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    # l.info(f"Request: {request.method} {request.url}")
    try:
        p = u.perf_counter()
        response: Response = await call_next(request)
        l.info(f"New request: {request.method} {request.url} - {response.status_code} ({p()}ms)")
        return response
    except Exception as e:
        l.exception(f"Request error: {request.method} {request.url} - {e} ({p()}ms)")
        raise

# endregion app

# region custom-docs

if c.enable_docs:
    @app.get('/docs', include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url or '/openapi.json',
            title=app.title,
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url='https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.27.1/swagger-ui-bundle.js',
            swagger_css_url='https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.27.1/swagger-ui.css',
        )

    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)  # type: ignore
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    @app.get('/redoc', include_in_schema=False)
    async def redoc_html():
        return get_redoc_html(
            openapi_url=app.openapi_url,  # type: ignore
            title=app.title + ' - ReDoc',
            redoc_js_url='https://unpkg.com/redoc@2/bundles/redoc.standalone.js',
        )

# endregion custom-docs

# region api

sites = ImgAPIInit()


class GetUrlFailedResponseModel(BaseModel):
    success: bool = False
    error: str = '获取跳转 URL 失败, 请重试 | Get redirect URL Failed, please retry'


api_responses = {
    302: {
        'description': ce('成功重定向到一个图片 URL', 'Successful redirect to an image URL'),
        'headers': {
            'X-ImgAPI-Version': {
                'description': ce('ImgAPI 版本', 'ImgAPI version'),
                'schema': {'type': 'string'}
            },
            'X-ImgAPI-Site-Id': {
                'description': ce('图片 API 站点的 ID', 'ID of the site providing the image'),
                'schema': {'type': 'string'}
            },
            'X-ImgAPI-Node': {
                'description': ce('ImgAPI 节点 IP', 'ImgAPI Node ID'),
                'schema': {'type': 'string'}
            }
        }
    },
    503: {
        'description': ce('获取跳转 URL 失败', 'Failed to get redirect url'),
        'model': GetUrlFailedResponseModel,
        'headers': {
            'X-ImgAPI-Version': {
                'description': ce('ImgAPI 版本', 'ImgAPI version'),
                'schema': {'type': 'string'}
            },
            'X-ImgAPI-Node': {
                'description': ce('ImgAPI 节点 IP', 'ImgAPI Node ID'),
                'schema': {'type': 'string'}
            }
        }
    }
}

api_responses_auto = {
    **api_responses,
    302: {
        'description': ce('成功重定向到一个图片 URL', 'Successful redirect to an image URL'),
        'headers': {
            'X-ImgAPI-Version': {
                'description': ce('ImgAPI 版本', 'ImgAPI version'),
                'schema': {'type': 'string'}
            },
            'X-ImgAPI-Site-Id': {
                'description': ce('图片 API 站点的 ID', 'ID of the site providing the image'),
                'schema': {'type': 'string'}
            },
            'X-ImgAPI-UA-Result': {
                'description': ce('User-Agent 判断结果 (horizontal, vertical 或 unknown)', 'User-Agents parse results (horizontal, vertical or unknown)'),
                'schema': {'type': 'string'}
            },
            'X-ImgAPI-Node': {
                'description': ce('ImgAPI 节点 IP', 'ImgAPI Node ID'),
                'schema': {'type': 'string'}
            }
        }
    }
}


@app.get(
    '/image',
    response_class=RedirectResponse,
    name='Get Image',
    description=ce('获取图片 (由 ImgAPI 决定类型)', 'Get an image (type processed by ImgAPI)'),
    status_code=302,
    responses=api_responses_auto  # type: ignore
)
def image(req: Request):
    ua_str: str | None = req.headers.get('User-Agent', None)
    if ua_str:
        ua = parse_ua(ua_str)
        if ua.is_mobile:
            # Mobile -> Vertical
            resp = image_vertical(req)
            result = 'vertical'
        elif ua.is_pc or ua.is_tablet:
            # PC / Tablet -> Horizontal
            resp = image_horizontal(req)
            result = 'horizontal'
        else:
            # Unknown -> Auto
            resp = image_auto(req)
            result = 'unknown'
    else:
        resp = image_auto(req)
        result = 'unknown'
    resp.headers['X-ImgAPI-UA-Result'] = result
    return resp


def image_auto(req: Request):
    site_list = sites.allow_a.copy()
    while site_list.count != 0:
        site = choice(site_list)
        url = site.auto(req)
        if url:
            return RedirectResponse(
                url,
                status_code=302,
                headers={
                    'X-ImgAPI-Version': VERSION,
                    'X-ImgAPI-Node': c.node,
                    'X-ImgAPI-Site-Id': site.id
                }
            )
        else:
            site_list.remove(site)
    return Response(
        GetUrlFailedResponseModel(),
        status_code=503,
        headers={
            'X-ImgAPI-Version': VERSION,
            'X-ImgAPI-Node': c.node
        }
    )


@app.get(
    '/image/h',
    response_class=RedirectResponse,
    name='Get Image Horizontal',
    description=ce('获取图片 (横向)', 'Get an image (Horizontal)'),
    status_code=302,
    responses=api_responses  # type: ignore
)
def image_horizontal(req: Request):
    site_list = sites.allow_h.copy()
    while site_list.count != 0:
        site = choice(site_list)
        url = site.horizontal(req)
        if url:
            return RedirectResponse(
                url,
                status_code=302,
                headers={
                    'X-ImgAPI-Version': VERSION,
                    'X-ImgAPI-Site-Id': site.id,
                    'X-ImgAPI-Node': c.node
                }
            )
        else:
            site_list.remove(site)
    return Response(
        GetUrlFailedResponseModel(),
        status_code=503,
        headers={
            'X-ImgAPI-Version': VERSION,
            'X-ImgAPI-Node': c.node
        }
    )


@app.get(
    '/image/v',
    response_class=RedirectResponse,
    name='Get Image Vertical',
    description=ce('获取图片 (竖向)', 'Get an image (Vertical)'),
    status_code=302,
    responses=api_responses  # type: ignore
)
def image_vertical(req: Request):
    site_list = sites.allow_v.copy()
    while site_list.count != 0:
        site = choice(site_list)
        url = site.vertical(req)
        if url:
            return RedirectResponse(
                url,
                status_code=302,
                headers={
                    'X-ImgAPI-Version': VERSION,
                    'X-ImgAPI-Node': c.node,
                    'X-ImgAPI-Site-Id': site.id
                }
            )
        else:
            site_list.remove(site)
    return Response(
        GetUrlFailedResponseModel(),
        status_code=503,
        headers={
            'X-ImgAPI-Version': VERSION,
            'X-ImgAPI-Node': c.node
        }
    )

# endregion api

# region fallback


@app.get('/{path:path}', include_in_schema=False)
async def fallback(path: str, req: Request):
    match path:
        case '/img' | '/img/s' | '/image/s':
            return image(req)
        case '/img/h':
            return image_horizontal(req)
        case '/img/v':
            return image_vertical(req)
        case _:
            return Response(
                'Not Found',
                404,
                headers={
                    'X-ImgAPI-Version': VERSION,
                    'X-ImgAPI-Node': c.node
                }
            )

# endregion fallback

# region root


class RootResponseModel(BaseModel):
    hello: str = 'imgapi'
    version: str = VERSION
    node: str = c.node
    repo: str = 'https://github.com/siiway/imgapi'


if c.root_redirect:
    @app.get(
        '/',
        status_code=302,
        description=ce(f'重定向到 {c.root_redirect}', f'Redirect to {c.root_redirect}'),
        response_class=RedirectResponse
    )
    def root_redirect():
        return RedirectResponse(c.root_redirect or '', status_code=302)
else:
    @app.get(
        '/',
        status_code=200,
        description=ce('返回 ImgAPI 版本号和信息', 'Return ImgAPI Version and information'),
        response_model=RootResponseModel,
    )
    def root():
        return RootResponseModel()

# endregion root

if __name__ == '__main__':
    run('main:app', host=c.host, port=c.port, workers=c.workers)

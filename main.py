import logging
from random import choice
from sys import stderr
import typing as t
from uuid import uuid4 as uuid
from contextvars import ContextVar
from mimetypes import guess_type
from pathlib import Path
from os.path import join as join_path

from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html
from pydantic import BaseModel, ValidationError
from loguru import logger as l
from uvicorn import run
from fastapi.openapi.utils import get_openapi
from config import config as c, load_config_failed

import utils as u
from utils import cnen as ce
from imgapi import ImgAPIInit

VERSION = '2025.10.19'

# region init
new_init = u.InitOnceChecker().new_init

reqid: ContextVar[str] = ContextVar('imgapi_reqid', default='not-in-request')

if new_init:

    # init logger
    l.remove()

    # 定义日志格式，包含 reqid
    def log_format(record):
        reqid = record['extra'].get('reqid', 'fallback-logid')  # type: ignore - 从 extra 或 ContextVar 获取 reqid
        return '<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <yellow>' + reqid + '</yellow> | <cyan>{name}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>\n'

    l.add(
        stderr,
        level=c.log.level,
        format=log_format,
        backtrace=True,
        diagnose=True
    )

    if c.log.file:
        l.add(
            'logs/{time:YYYY-MM-DD}.log',
            level=c.log.level,
            format=log_format,
            colorize=False,
            rotation=c.log.rotation,
            retention=c.log.retention,
            enqueue=True
        )
    l.configure(extra={'reqid': 'not-in-request'})


class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = l.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())


logging.getLogger('uvicorn').handlers.clear()
logging.getLogger('uvicorn.access').handlers.clear()
logging.getLogger('uvicorn.error').handlers.clear()
logging.getLogger().handlers = [InterceptHandler()]
logging.getLogger().setLevel(c.log.level)
logging.getLogger('watchfiles').level = logging.WARNING

if new_init:

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

    sites = ImgAPIInit()

app = FastAPI(
    title=f'ImgAPI - {c.node}',
    description='一个简单的随机背景图 API, 基于 FastAPI | A simple random background image API based on FastAPI | https://github.com/siiway/imgapi | MIT License',
    version=VERSION,
    docs_url=None,
    redoc_url=None
)


@app.middleware('http')
async def log_requests(request: Request, call_next):
    request_id = str(uuid())
    token = reqid.set(request_id)
    with l.contextualize(reqid=request_id):
        if request.client:
            ip = f'[{request.client.host}]' if ':' in request.client.host else request.client.host
            port = request.client.port
        else:
            ip = 'unknown-ip'
            port = 0
        l.info(f'Incoming request: {ip}:{port} - {request.method} {request.url.path}')
        try:
            p = u.perf_counter()
            resp: Response = await call_next(request)
            l.info(f'Outgoing response: {resp.status_code} ({p()}ms)')
            return resp
        except Exception as e:
            l.error(f'Server error: {e} ({p()}ms)')
            resp = Response(f'Internal Server Error ({request_id}@{c.node})', 500)
        finally:
            resp.headers['X-ImgAPI-Version'] = VERSION
            resp.headers['X-ImgAPI-Node'] = c.node
            resp.headers['X-ImgAPI-Request-Id'] = request_id
            reqid.reset(token)
            return resp


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    for path in openapi_schema.get('paths', {}).values():
        for operation in path.values():
            if 'responses' not in operation:
                operation['responses'] = {}

            for status_code, response in operation['responses'].items():
                if isinstance(response, str):
                    operation['responses'][status_code] = {'description': response}

                if 'headers' not in operation['responses'][status_code]:
                    operation['responses'][status_code]['headers'] = {}

                operation['responses'][status_code]['headers'].setdefault(
                    'X-ImgAPI-Version', {
                        'description': ce('ImgAPI 版本', 'ImgAPI version'),
                        'schema': {'type': 'string'}
                    }
                )
                operation['responses'][status_code]['headers'].setdefault(
                    'X-ImgAPI-Node', {
                        'description': ce('ImgAPI 节点 ID', 'ImgAPI Node ID'),
                        'schema': {'type': 'string'}
                    }
                )
                operation['responses'][status_code]['headers'].setdefault(
                    'X-ImgAPI-Request-Id', {
                        'description': ce('ImgAPI 请求 ID', 'ImgAPI Request ID'),
                        'schema': {'type': 'string'}
                    }
                )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

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


class GetUrlFailedResponseModel(BaseModel):
    success: bool = False
    error: str = '获取跳转 URL 失败, 请重试 | Get redirect URL Failed, please retry'


api_responses = {
    302: {
        'description': ce('成功重定向到一个图片 URL', 'Successful redirect to an image URL'),
        'headers': {
            'X-ImgAPI-Site-Id': {
                'description': ce('图片 API 站点的 ID', 'ID of the site providing the image'),
                'schema': {'type': 'string'}
            }
        }
    },
    503: {
        'description': ce('获取跳转 URL 失败', 'Failed to get redirect url'),
        'model': GetUrlFailedResponseModel
    }
}

api_responses_auto = {
    **api_responses,
    302: {
        'description': ce('成功重定向到一个图片 URL', 'Successful redirect to an image URL'),
        'headers': {
            'X-ImgAPI-Site-Id': {
                'description': ce('图片 API 站点的 ID', 'ID of the site providing the image'),
                'schema': {'type': 'string'}
            },
            'X-ImgAPI-UA-Result': {
                'description': ce('User-Agent 判断结果 (horizontal, vertical 或 unknown)', 'User-Agents parse results (horizontal, vertical or unknown)'),
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
    result = u.ua(ua_str=ua_str) if ua_str else 'unknown'
    l.debug(f'User-Agent: {ua_str}, result: {result}')
    match result:
        case 'horizontal':
            resp = image_horizontal(req)
        case 'vertical':
            resp = image_vertical(req)
        case 'unknown' | _:
            resp = image_auto(req)
    resp.headers['X-ImgAPI-UA-Result'] = result
    return resp


def image_auto(req: Request):
    site_list = sites.allow_a.copy()
    while site_list.count != 0:
        site = choice(site_list)
        url = site.auto(req)
        l.debug(f'Try site {site.id} -> {url}, vaild: {True if url else False}')
        if url:
            return RedirectResponse(
                url,
                status_code=302,
                headers={
                    'X-ImgAPI-Site-Id': site.id
                }
            )
        else:
            site_list.remove(site)
    return Response(
        GetUrlFailedResponseModel(),
        status_code=503
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
        l.debug(f'Try site {site.id} -> {url}, vaild: {True if url else False}')
        if url:
            return RedirectResponse(
                url,
                status_code=302,
                headers={
                    'X-ImgAPI-Site-Id': site.id
                }
            )
        else:
            site_list.remove(site)
    return Response(
        GetUrlFailedResponseModel(),
        status_code=503
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
        l.debug(f'Try site {site.id} -> {url}, vaild: {True if url else False}')
        if url:
            return RedirectResponse(
                url,
                status_code=302,
                headers={
                    'X-ImgAPI-Site-Id': site.id
                }
            )
        else:
            site_list.remove(site)
    return Response(
        GetUrlFailedResponseModel(),
        status_code=503
    )


class UATestResponse(BaseModel):
    user_agent: str | None
    parsed: u.UAResult | None
    parse_error: str | None = None
    result: t.Literal['vertical', 'horizontal', 'unknown']


@app.get(
    '/ua',
    description=ce('测试 User-Agent 判断结果', 'Test User-Agent Process Result')
)
def ua_test(req: Request) -> UATestResponse:
    ua_str: str | None = req.headers.get('User-Agent', None)
    l.debug(f'User-Agent: {ua_str}, exists: {bool(ua_str)}')
    result = u.ua(ua_str=ua_str) if ua_str else 'unknown'
    error = None
    if ua_str:
        ua = u.parse_ua(ua_str)
        try:
            ua_parsed = u.UAResult(
                browser=u._UAResult_Browser(
                    family=ua.browser.family if ua.browser else None,
                    version=ua.browser.version if ua.browser else None,
                    version_string=ua.browser.version_string if ua.browser else None
                ),
                os=u._UAResult_OS(
                    family=ua.os.family if ua.os else None,
                    version=ua.os.version if ua.os else None,
                    version_string=ua.os.version_string if ua.os else None
                ),
                device=u._UAResult_Device(
                    family=ua.device.family if ua.device else None,
                    brand=ua.device.brand if ua.device else None,
                    model=ua.device.model if ua.device else None
                ),
                is_bot=ua.is_bot,
                is_email_client=ua.is_email_client,
                is_mobile=ua.is_mobile,
                is_pc=ua.is_pc,
                is_tablet=ua.is_tablet,
                is_touch_capable=ua.is_touch_capable
            )
        except ValidationError as e:
            ua_parsed = None
            l.warning(f'Parse error: {e}')
            error = str(e)
    else:
        ua_parsed = None
    return UATestResponse(
        user_agent=ua_str,
        parsed=ua_parsed,
        parse_error=error,
        result=result
    )

# endregion api

# region fallback


@app.get('/{path:path}', include_in_schema=False)
async def fallback(path: str, req: Request):
    if path:
        file_path = u.get_path(join_path('public', path))
        file = Path(file_path)
        if file.is_file():
            mime_type, _ = guess_type(file)
            l.info(f'Serving static file: {file_path}')
            return FileResponse(
                path=file_path,
                headers={
                    'X-ImgAPI-Version': VERSION,
                    'X-ImgAPI-Node': c.node,
                    'X-ImgAPI-Request-Id': reqid.get()
                },
                media_type=mime_type or 'application/octet-stream'
            )
        else:
            l.debug(f'Static file not found: {file_path}')

    match path:
        case 'img' | 'img/s' | 'image/s':
            return image(req)
        case 'img/h':
            return image_horizontal(req)
        case 'img/v':
            return image_vertical(req)
        case 'about':
            return ua_test(req)
        case _:
            l.debug(f'Path not found: {path}')
            return Response(
                'Not Found',
                status_code=404,
                headers={
                    'X-ImgAPI-Version': VERSION,
                    'X-ImgAPI-Node': c.node,
                    'X-ImgAPI-Request-Id': reqid.get()
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
    l.debug('Root redirect -> True')

    @app.get(
        '/',
        status_code=302,
        description=ce(f'重定向到 {c.root_redirect}', f'Redirect to {c.root_redirect}'),
        response_class=RedirectResponse
    )
    def root_redirect():
        return RedirectResponse(c.root_redirect or '', status_code=302)
else:
    l.debug('Root redirect -> False')

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
    l.info(f'Starting server: {f"[{c.host}]" if ":" in c.host else c.host}:{c.port} with {c.workers} workers')
    run('main:app', host=c.host, port=c.port, workers=c.workers)
    print()
    l.info('Bye.')

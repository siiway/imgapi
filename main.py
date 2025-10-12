import logging
from logging.handlers import RotatingFileHandler
from random import choice

from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html
from pydantic import BaseModel
from user_agents import parse as parse_ua

from config import config as c
import utils as u
from utils import cnen as ce
from imgapi import ImgAPIInit

VERSION = '2025.10.13'

# region init

# init logger
loglvl = getattr(logging, c.log.level.upper(), logging.INFO)
l = logging.getLogger('uvicorn')  # get logger
logging.basicConfig(level=loglvl)  # log level
l.level = loglvl  # set logger level
root_logger = logging.getLogger()  # get root logger
root_logger.handlers.clear()  # clear default handlers
stream_handler = logging.StreamHandler()  # get stream handler
# stream_handler.setFormatter(u.CustomFormatter())  # set stream formatter
# set file handler
if c.log.file:
    log_file_path = u.get_path(c.log.file)
    if c.log.rotating:
        file_handler = RotatingFileHandler(
            log_file_path, encoding='utf-8', errors='ignore', maxBytes=int(c.log.rotating_size * 1024), backupCount=c.log.rotating_count
        )
    else:
        file_handler = logging.FileHandler(log_file_path, encoding='utf-8', errors='ignore')
    # file_handler.setFormatter(u.CustomFormatter())
    root_logger.addHandler(file_handler)
logging.getLogger('watchfiles').level = logging.WARNING  # set watchfiles logger level

# endregion init

# region app

l.info(f'{'='*25} Application Startup {'='*25}')

l.info(f'''ImgAPI v{VERSION} by SiiWay Team
Under MIT License
GitHub: https://github.com/siiway/imgapi''')

app = FastAPI(
    title='ImgAPI',
    description='一个简单的随机背景图 API, 基于 FastAPI | A simple random background image API based on FastAPI | https://github.com/siiway/imgapi',
    version=VERSION,
    docs_url=None,
    redoc_url=None
)

# endregion app

# region custom-docs

if c.enable_docs:
    @app.get('/docs', include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,  # type: ignore
            title=app.title + ' - Swagger UI',
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
            }
        }
    }
}

api_responses_self = {
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
    responses=api_responses_self  # type: ignore
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


@app.get(
    '/image/a',
    response_class=RedirectResponse,
    name='Get Image Auto',
    description=ce('获取图片 (由目标 API 决定类型)', 'Get an image (type processed by target API itself)'),
    status_code=302,
    responses=api_responses  # type: ignore
)
def image_auto(req: Request):
    site_list = sites.allow_a.copy()
    failed: list[str] = []
    while site_list.count != 0:
        site = choice(site_list)
        url = site.auto(req)
        if url:
            return RedirectResponse(
                url,
                status_code=302,
                headers={
                    'X-ImgAPI-Version': VERSION,
                    'X-ImgAPI-Site-Id': site.id
                }
            )
        else:
            failed.append(site.id)
    return Response(
        GetUrlFailedResponseModel(),
        status_code=503,
        headers={
            'X-ImgAPI-Version': VERSION
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
    failed: list[str] = []
    while site_list.count != 0:
        site = choice(site_list)
        url = site.horizontal(req)
        if url:
            return RedirectResponse(
                url,
                status_code=302,
                headers={
                    'X-ImgAPI-Version': VERSION,
                    'X-ImgAPI-Site-Id': site.id
                }
            )
        else:
            failed.append(site.id)
    return Response(
        GetUrlFailedResponseModel(),
        status_code=503,
        headers={
            'X-ImgAPI-Version': VERSION
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
    site_list = sites.allow_h.copy()
    failed: list[str] = []
    while site_list.count != 0:
        site = choice(site_list)
        url = site.vertical(req)
        if url:
            return RedirectResponse(
                url,
                status_code=302,
                headers={
                    'X-ImgAPI-Version': VERSION,
                    'X-ImgAPI-Site-Id': site.id
                }
            )
        else:
            failed.append(site.id)
    return Response(
        GetUrlFailedResponseModel(),
        status_code=503,
        headers={
            'X-ImgAPI-Version': VERSION
        }
    )

# endregion api

# region root


class RootResponseModel(BaseModel):
    hello: str = 'imgapi'
    version: str = VERSION
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

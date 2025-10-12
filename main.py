import logging
from logging.handlers import RotatingFileHandler
from random import choice

from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html
from pydantic import BaseModel

from config import config as c
import utils as u
from imgapi import ImgAPIInit

VERSION = '2025.10.12'

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

l.info(f'{"="*25} Application Startup {"="*25}')

l.info(f'''ImgAPI v{VERSION} by SiiWay Team
Under MIT License
GitHub: https://github.com/siiway/imgapi''')

app = FastAPI(
    title='ImgAPI',
    description='A simple random background image API based on FastAPI | https://github.com/siiway/imgapi',
    version=VERSION,
    docs_url=None,
    redoc_url=None
)

# endregion app

# region custom-docs

if c.enable_docs:
    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,  # type: ignore
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.27.1/swagger-ui-bundle.js",
            swagger_css_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.27.1/swagger-ui.css",
        )

    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)  # type: ignore
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    @app.get("/redoc", include_in_schema=False)
    async def redoc_html():
        return get_redoc_html(
            openapi_url=app.openapi_url,  # type: ignore
            title=app.title + " - ReDoc",
            redoc_js_url="https://unpkg.com/redoc@2/bundles/redoc.standalone.js",
        )

# endregion custom-docs

# region api

sites = ImgAPIInit()


@app.get('/image', response_class=RedirectResponse, responses={502: {
    'content': None,
    'headers': {}
}})
def image_auto(req: Request):
    retries = c.max_retries
    failed: list[str] = []
    while retries > 0:
        retries -= 1
        site = choice(sites.allow_a)
        url = site.auto(req)
        if url:
            return RedirectResponse(url, status_code=302, headers={
                'X-ImgAPI-Version': VERSION,
                'X-ImgAPI-Site-Id': site.id,
                'X-ImgAPI-Tries': str(c.max_retries - retries)
            })
        else:
            failed.append(site.id)
    return Response('', status_code=502, headers={
        'X-ImgAPI-Version': VERSION,
        'X-ImgAPI-Failed-Site-Ids': str(failed),
        'X-ImgAPI-Max-Tries': str(c.max_retries)
    })

# endregion api

# region root


class RootResponseModel(BaseModel):
    hello: str = 'imgapi'
    version: str = VERSION


if c.root_redirect:
    @app.get(
        '/',
        status_code=302,
        description=f'重定向到 {c.root_redirect}<br/><i>Redirect to {c.root_redirect}</i>',
        response_class=RedirectResponse
    )
    def root_redirect():
        return RedirectResponse(c.root_redirect or '', status_code=302)
else:
    @app.get(
        '/',
        status_code=200,
        description='显示 ImgAPI 版本号<br/><i>Show ImgAPI Version</i>',
        response_model=RootResponseModel,
    )
    def root():
        return RootResponseModel()

# endregion root

import logging
from logging.handlers import RotatingFileHandler

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html

from config import config as c
import utils as u

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
stream_handler.setFormatter(u.CustomFormatter())  # set stream formatter
# set file handler
if c.log.file:
    log_file_path = u.get_path(c.log.file)
    if c.log.rotating:
        file_handler = RotatingFileHandler(
            log_file_path, encoding='utf-8', errors='ignore', maxBytes=int(c.log.rotating_size * 1024), backupCount=c.log.rotating_count
        )
    else:
        file_handler = logging.FileHandler(log_file_path, encoding='utf-8', errors='ignore')
    file_handler.setFormatter(u.CustomFormatter())
    root_logger.addHandler(file_handler)
logging.getLogger('watchfiles').level = logging.WARNING  # set watchfiles logger level

# endregion init

# region app

l.info(f'{"="*20} Application Startup {"="*20}')

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


@app.get('/')
def root():
    return RedirectResponse(c.root_redirect, 301)

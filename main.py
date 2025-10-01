import logging
from logging.handlers import RotatingFileHandler

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

from config import config as c
import utils as u
VERSION = '2025.10.01'

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


l.info(f'{"="*15} Application Startup {"="*15}')

l.info(f'''ImgAPI v{VERSION} by SiiWay Team
Under MIT License
GitHub: https://github.com/siiway/imgapi''')

app = FastAPI(
    title='ImgAPI',
    description='A simple random background image API based on FastAPI and redirect | https://github.com/siiway/imgapi',
    debug=c.debug,
    version=VERSION
)


@app.get('/')
def root():
    return RedirectResponse('/docs', 301)


if __name__ == '__main__':
    uvicorn.run(app, host=c.host, port=c.port)

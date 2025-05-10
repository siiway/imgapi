# coding: utf-8
import os
import json

if os.path.exists('config.json'):
    try:
        with open('config.json', 'r') as f:
            conf: dict = json.load(f)
            f.close()
    except Exception as e:
        print(f'Load config.json error: {e}, fallback to default')
        conf = {}
else:
    conf = {}

host: str = conf.get('host', '0.0.0.0')
port: int = conf.get('port', 9333)
debug: bool = conf.get('debug', False)

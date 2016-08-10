import logging
import requests


class SpaceHandler(logging.Handler):
    def __init__(self, src, *args, **kwargs):
        self.src = src
        super().__init__(*args, **kwargs)

    def emit(self, record):
        resp = requests.post('http://127.0.0.1:8000/login/',
                             {'username': 'admin', 'password': '123456nn'})
        # data=dict(username='admin', password='123456nn'))

        cookies = dict(sessionid=resp.cookies['sessionid'])
        response_two = requests.post(self.src, cookies=cookies,
                                     data={'level': record.levelname,
                                           'name_logger': record.name,
                                           'message': record.msg})

logger = logging.getLogger('logger')
logger.setLevel("DEBUG")

space_handler = SpaceHandler('http://127.0.0.1:8000')
space_handler.setLevel("DEBUG")

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to space_handler
space_handler.setFormatter(formatter)

# add space_handler to logger
logger.addHandler(space_handler)

logger.info('success')

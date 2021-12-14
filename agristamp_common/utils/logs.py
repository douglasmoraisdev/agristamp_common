import json
import logging
import os

class DefaultsLogFilter(logging.Filter):
    def filter(self, record):

        try:
            if not hasattr(record, 'error_type'):
                record.error_type = ''

            if not hasattr(record, 'value'):
                record.value = ''

            if not hasattr(record, 'status_code'):
                record.status_code = ''

        except KeyError as ke:
            return True

        return True

STAGE = os.getenv('STAGE', 'unknow')
SERVICE_SLUG = os.getenv('SERVICE_SLUG', 'unknow')

FORMAT = json.dumps({
    'type': 'service_log',
    'stage': STAGE,
    'service_slug': SERVICE_SLUG,
    'log_level': '%(levelname)s',
    'message': '%(message)s',
    'error_type': '%(error_type)s',
    'value': '%(value)s',
    'status_code': '%(status_code)s'
})


logging.basicConfig(format=FORMAT)

logger = logging.getLogger()

log_level = os.getenv('LOG_LEVEL') or logging.ERROR

logger.setLevel(log_level)
logger.addFilter(DefaultsLogFilter())
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(log_level)
ch.addFilter(DefaultsLogFilter())


# create formatter and add it to the handlers
formatter = logging.Formatter(FORMAT)
ch.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)

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

            if not hasattr(record, 'error_code'):
                record.error_code = ''

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
    'error_code': '%(error_code)s',
    'value': '%(value)s',
    'status_code': '%(status_code)s'
})
LOG_LEVEL = os.getenv('LOG_LEVEL') or logging.ERROR


# fora do stage local seta todos os logs para CRITICAL
if STAGE != 'local':
    [logging.getLogger(key).setLevel(logging.CRITICAL)
    for index, key in enumerate(logging.root.manager.loggerDict)]


logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)
logger.addFilter(DefaultsLogFilter())

# create Console Handler
ch = logging.StreamHandler()
ch.setLevel(LOG_LEVEL)
ch.addFilter(DefaultsLogFilter())

# create formatter and add it to the handlers
ch.setFormatter(logging.Formatter(FORMAT))

# add the handlers to logger
if (logger.hasHandlers()):
    logger.handlers.clear()

logger.addHandler(ch)

import logging
import os

STAGE = os.getenv('STAGE', 'unknow')
FORMAT = f'[service_log][{STAGE}] %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger()

log_level = os.getenv('LOG_LEVEL') or logging.ERROR

logger.setLevel(log_level)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(log_level)

# Level name as String
str_level = logging.getLevelName(logger.getEffectiveLevel())

# create formatter and add it to the handlers
formatter = logging.Formatter(f'[service_log][{STAGE}][{str_level}] %(message)s')
ch.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)

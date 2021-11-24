import logging
import os

STAGE = os.getenv('STAGE', 'unknow')
FORMAT = f'[service_log][{STAGE}] %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger()

log_level = os.getenv('LOG_LEVEL') or logging.ERROR

logger.setLevel(log_level)

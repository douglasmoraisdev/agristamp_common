import logging
import os
logger = logging.getLogger()

log_level = os.getenv('LOG_LEVEL') or logging.ERROR

stage = os.getenv('STAGE', 'unknow')

FORMAT = f'[service_log][{stage}] xyz %(message)s'
logging.basicConfig(format=FORMAT)

logger.setLevel(log_level)

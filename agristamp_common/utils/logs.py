import logging
import os
logger = logging.getLogger()

log_level = os.getenv('LOG_LEVEL') or logging.ERROR

FORMAT = '[service_log]: %(message)s'
logging.basicConfig(format=FORMAT)

logger.setLevel(log_level)

import logging
import os
logger = logging.getLogger()

log_level = os.getenv('LOG_LEVEL') or logging.ERROR

logger.setLevel(logging.INFO)

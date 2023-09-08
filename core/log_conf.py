import logging
from logging.handlers import RotatingFileHandler


def create_logger(name, filename):
    logger = logging.getLogger(name)
    handler = RotatingFileHandler(filename, maxBytes=10000, backupCount=1)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

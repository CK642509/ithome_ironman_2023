from loguru import logger
import sys

def init_logger():
    fmt = "{time} - {name} - {level} - {message}"
    logger.add("spam.log", level="DEBUG", format=fmt)
    logger.add(sys.stderr, level="ERROR", format=fmt)
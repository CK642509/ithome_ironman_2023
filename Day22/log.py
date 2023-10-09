from loguru import logger
import sys

# def init_logger():
#     fmt = "{time} - {name} - {level} - {message}"
#     logger.add("spam.log", level="DEBUG", format=fmt)
#     logger.add(sys.stderr, level="ERROR", format=fmt)
#     logger.add("out.log", backtrace=True, diagnose=True)

logger.add("out.log", backtrace=True, diagnose=True)

def func(a, b):
    return a / b

def test(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

test(0)

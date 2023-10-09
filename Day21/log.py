import logging

# class InterceptHandler(logging.Handler):
#     """
#     Default handler from examples in loguru documentaion.
#     See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
#     """

#     def emit(self, record: logging.LogRecord):
#         # Get corresponding Loguru level if it exists
#         try:
#             level = logger.level(record.levelname).name
#         except ValueError:
#             level = record.levelno

#         # Find caller from where originated the logged message
#         frame, depth = logging.currentframe(), 2
#         while frame.f_code.co_filename == logging.__file__:
#             frame = frame.f_back
#             depth += 1

#         logger.opt(depth=depth, exception=record.exc_info).log(
#             level, record.getMessage()
#         )

def init_logging():
    logger = logging.getLogger("uvicorn")
    logger.handlers = []

    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    fh = logging.FileHandler(filename='example2.log')
    formatter = logging.Formatter("%(asctime)s %(message)s")

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
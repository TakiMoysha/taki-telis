import logging


__all__ = ["create_logger"]


logging.basicConfig(level=logging.INFO)


def create_logger():
    logger = logging.getLogger(__name__)

    return logger

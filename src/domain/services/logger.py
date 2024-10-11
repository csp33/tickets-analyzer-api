import logging
import sys


class LoggerService:
    @staticmethod
    def get_logger() -> logging.Logger:
        logger = logging.getLogger("tickets_analyzer_api")
        logger.setLevel(logging.DEBUG)
        if not logger.hasHandlers():
            stream_handler = logging.StreamHandler(sys.stdout)
            log_formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            stream_handler.setFormatter(log_formatter)
            logger.addHandler(stream_handler)
        return logger

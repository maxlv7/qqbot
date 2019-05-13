import logging
import sys

LOGGING_CONFIG_DEFAULTS = dict(
    version=1,
    disable_existing_loggers=False,
    loggers={
        "qqbot": {"level": "DEBUG", "handlers": ["console"]},
    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout,
        }
    },
    formatters={
        "generic": {
            "format": "%(asctime)s [%(levelname)s] [%(filename)s] [%(funcName)s] >>> %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter",
        },
    }
)

botLog = logging.getLogger("qqbot")

import logging.config
logging.config.dictConfig(LOGGING_CONFIG_DEFAULTS)



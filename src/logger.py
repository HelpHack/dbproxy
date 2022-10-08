import logging
from colorlog import ColoredFormatter
from pymongo import monitoring
from mongoengine import *

class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: grey,
        logging.INFO: grey,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red
    }

    def use_format(self, color):
        return ' - '.join([
            '%(asctime)s',
            ''.join(['[', color, '%(levelname)s', self.reset, ']']),
            '%(message)s (%(filename)s:%(lineno)d)'   
        ])

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(self.use_format(log_fmt))
        return formatter.format(record)

class Logger:
    logger = logging.getLogger('logger')

    def __init__(self):
        # Create the main logger
        Logger.logger.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(CustomFormatter())
        # Add the console handler to the logger
        Logger.logger.addHandler(ch)

    def debug(msg = ''):
        Logger.logger.debug(msg)

    def error(msg = ''):
        Logger.logger.error(msg)

class CommandLogger(monitoring.CommandListener):

    def started(self, event):
        Logger.debug("Command {0.command_name} with request id "
                 "{0.request_id} started on server "
                 "{0.connection_id}".format(event))

    def succeeded(self, event):
        Logger.debug("Command {0.command_name} with request id "
                 "{0.request_id} on server {0.connection_id} "
                 "succeeded in {0.duration_micros} "
                 "microseconds".format(event))

    def failed(self, event):
        Logger.error("Command {0.command_name} with request id "
                 "{0.request_id} on server {0.connection_id} "
                 "failed in {0.duration_micros} "
                 "microseconds".format(event))

monitoring.register(CommandLogger())
Logger()
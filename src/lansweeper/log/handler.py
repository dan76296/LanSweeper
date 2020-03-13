import logging
import inspect

from datetime import datetime
from pathlib import Path
from sys import stdout, _getframe
from logging.handlers import TimedRotatingFileHandler


class Handler:

    log_directory = "%s/logs" % (Path(__file__).parents[2])

    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console = logging.StreamHandler(stdout)
    console.setFormatter(log_format)

    log_level = logging.INFO
    log_name = 'lansweeper'  # Add project name here

    def __init__(self):
        self.start_log()
        pass

    def start_log(self):
        self.log = logging.getLogger(self.log_name)
        self.log.addHandler(self.console)
        self.log.setLevel(self.log_level)
        self.log.propagate = False
        pass

    def set_log_file_name(self, log_filename):
        self.log_file_path = "%s/%s-%s.log" % \
            (self.log_directory,
             log_filename,
             (datetime.now().isoformat(timespec='seconds').replace(':', '-')))

        if not Path(self.log_directory).is_dir():
            Path(self.log_directory).mkdir

        self.log_file = TimedRotatingFileHandler(self.log_file_path,
                                                 when="midnight")
        self.log_file.setFormatter(self.log_format)

        self.log.addHandler(self.log_file)
        self.log.setLevel(self.log_level)
        self.log.propagate = False
        pass

    def set_log_level(self, log_level):
        self.log.setLevel(log_level)
        self.log_level = log_level
        pass

    def info(self, message):
        try:
            script_path = Path(
                    (inspect.stack()[1].filename)).relative_to(Path.cwd())
        except:
            script_path = inspect.stack()[1].filename

        if hasattr(self, 'log'):

            self.log.info("%s - %s: %s" % (
                script_path, inspect.stack()[1].lineno, message))
        else:
            print('%s - call set_log_name first' % (script_path))
        pass

    def debug(self, message):
        try:
            script_path = Path(
                    (inspect.stack()[1].filename)).relative_to(Path.cwd())
        except:
            script_path = inspect.stack()[1].filename

        if hasattr(self, 'log'):

            self.log.debug("%s - %s: %s" % (
                script_path, inspect.stack()[1].lineno, message))
        else:
            print('%s - call set_log_name first' % (script_path))
        pass

    def error(self, message):
        try:
            script_path = Path(
                    (inspect.stack()[1].filename)).relative_to(Path.cwd())
        except:
            script_path = inspect.stack()[1].filename

        if hasattr(self, 'log'):

            self.log.error("%s - %s: %s" % (
                script_path, inspect.stack()[1].lineno, message))
        else:
            print('%s - call set_log_name first' % (script_path))
        pass

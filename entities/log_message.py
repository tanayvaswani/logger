import threading

from datetime import datetime

from .log_level import LogLevel


class LogMessage:
    def __init__(self, level: LogLevel, logger: str, message: str):
        self.timestamp = datetime.now()
        self.level = level
        self.logger = logger
        self.message = message
        self.thread_name = threading.current_thread().name

    def get_timestamp(self) -> datetime:
        return self.timestamp

    def get_level(self) -> LogLevel:
        return self.level

    def get_logger(self) -> str:
        return self.logger

    def get_message(self) -> str:
        return self.message

    def get_thread_name(self) -> str:
        return self.thread_name

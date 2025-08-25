from entities.log_appender import LogAppender
from entities.log_formatter import LogFormatter, TextFormatter
from entities.log_message import LogMessage


class ConsoleAppender(LogAppender):
    def __init__(self):
        self.formatter = TextFormatter()

    def append(self, log_message: LogMessage):
        print(self.formatter.format(log_message), end='')

    def close(self):
        pass

    def set_formatter(self, formatter: LogFormatter):
        self.formatter = formatter

    def get_formatter(self) -> LogFormatter:
        return self.formatter

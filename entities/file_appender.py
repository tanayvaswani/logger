import threading

from entities.log_appender import LogAppender
from entities.log_formatter import LogFormatter, TextFormatter
from entities.log_message import LogMessage


class FileAppender(LogAppender):
    def __init__(self, file_path: str):
        self.formatter = TextFormatter()
        self._lock = threading.Lock()
        try:
            self.writer = open(file_path, 'a')
        except Exception as e:
            print(f"Failed to create writer for file logs, exception: {e}")
            self.writer = None

    def append(self, log_message: LogMessage):
        with self._lock:
            if self.writer:
                try:
                    self.writer.write(
                        self.formatter.format(log_message) + "\n")
                    self.writer.flush()
                except Exception as e:
                    print(f"Failed to write logs to file, exception: {e}")

    def close(self):
        if self.writer:
            try:
                self.writer.close()
            except Exception as e:
                print(f"Failed to close logs file, exception: {e}")

    def set_formatter(self, formatter: LogFormatter):
        self.formatter = formatter

    def get_formatter(self) -> LogFormatter:
        return self.formatter

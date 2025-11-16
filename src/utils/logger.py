"""
Logger com timestamp para feedback ao usuário
"""
from datetime import datetime
from enum import Enum

class LogLevel(Enum):
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"
    SEARCH = "SEARCH"
    ACTION = "ACTION"

class Logger:
    @staticmethod
    def log(message, level=LogLevel.INFO):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        level_str = level.value if isinstance(level, LogLevel) else level
        print(f"[{timestamp}] {level_str}: {message}")
    
    @staticmethod
    def info(message):
        Logger.log(message, LogLevel.INFO)
    
    @staticmethod
    def success(message):
        Logger.log(message, LogLevel.SUCCESS)
    
    @staticmethod
    def warning(message):
        Logger.log(message, LogLevel.WARNING)
    
    @staticmethod
    def error(message):
        Logger.log(message, LogLevel.ERROR)
    
    @staticmethod
    def debug(message):
        Logger.log(message, LogLevel.DEBUG)
    
    @staticmethod
    def search(message):
        Logger.log(message, LogLevel.SEARCH)
    
    @staticmethod
    def action(message):
        Logger.log(message, LogLevel.ACTION)

logger = Logger()

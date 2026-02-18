"""
logging.py
---------
This module provides a clean and readable logging system for the aetherai application.

Logs will use the following format:
[<module_name>] [<log_level>] <timestamp> - <message>
"""

import logging
import os
import sys
from datetime import datetime
from typing import Optional
import colorama

# Initialize colorama
colorama.init(autoreset=True)

# Define log levels
LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

# Color mapping for log levels
LOG_COLORS = {
    "DEBUG": colorama.Fore.CYAN,
    "INFO": colorama.Fore.GREEN,
    "WARNING": colorama.Fore.YELLOW,
    "ERROR": colorama.Fore.RED,
    "CRITICAL": colorama.Fore.MAGENTA,
}


class ColoredFormatter(logging.Formatter):
    """Custom formatter to apply colors and custom formatting."""

    def format(self, record: logging.LogRecord) -> str:
        level_name = record.levelname
        color = LOG_COLORS.get(level_name, "")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        formatted = f"[{record.name}] [{level_name}] {timestamp} - {record.getMessage()}"
        return f"{color}{formatted}{colorama.Style.RESET_ALL}"


def configure_logging(
    level: str = "INFO",
    log_file: Optional[str] = None,
    use_colors: bool = True,
) -> None:
    """
    Configure the global logging settings.

    Args:
        level (str): Logging level name.
        log_file (str, optional): Path to a file to write logs to.
        use_colors (bool): Whether to use colored output in console.
    """
    log_level = LOG_LEVELS.get(level.upper(), logging.INFO)

    # Clear existing handlers to avoid duplicates
    logging.getLogger().handlers.clear()
    logging.getLogger().setLevel(log_level)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    if use_colors:
        console_handler.setFormatter(ColoredFormatter())
    else:
        console_handler.setFormatter(
            logging.Formatter("[%(name)s] [%(levelname)s] %(asctime)s - %(message)s")
        )
    logging.getLogger().addHandler(console_handler)

    # Optional file handler
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(
            logging.Formatter("[%(name)s] [%(levelname)s] %(asctime)s - %(message)s")
        )
        logging.getLogger().addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    """
    Retrieve a logger for a specific module.

    Args:
        name (str): Name of the module or component.

    Returns:
        logging.Logger: Configured logger instance.
    """
    return logging.getLogger(name)
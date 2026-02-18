"""
main.py
---------
This is the main entry point for the aetherai application
It will be responsible for starting the application and handling the main loop
"""

import os
import sys
import time

from utils.logging import configure_logging, get_logger

configure_logging(level="DEBUG", log_file="aetherai.log")

logger = get_logger(__name__)

logger.info("Starting aetherai application")

def main():
    logger.info("Starting main loop")
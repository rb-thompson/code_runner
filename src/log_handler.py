# src/log_handler.py
import logging
import os

def get_logger(name):
    # Create logger with the specified name
    logger = logging.getLogger(name)
    
    # Check if handlers already exist to avoid duplicate logs
    if logger.hasHandlers():
        return logger

    # Define the standard format for logs
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create file handler which logs messages
    log_file = os.path.join(os.path.dirname(__file__), 'game.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(log_format)

    # Create console handler for stdout
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Set the logging level to INFO for both handlers
    logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.DEBUG)

    return logger
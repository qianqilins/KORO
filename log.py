import logging, time

mclog = f'[log]mc_{time.strftime("%Y%m%d_%H%M%S")}.log'
zslog = f'[log]zs_{time.strftime("%Y%m%d_%H%M%S")}.log'

def setup_logger(logfile):
    logger = logging.getLogger()
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')

        file_handler = logging.FileHandler(logfile)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

def mc_message(message, logfile=mclog):
    setup_logger(logfile)
    logging.info(message)

def zs_message(message, logfile=zslog):
    setup_logger(logfile)
    logging.info(message)

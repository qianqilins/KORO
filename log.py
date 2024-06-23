import logging, time, os

mc_log = f'[log]mc_{time.strftime("%Y%m%d_%H%M%S")}.log'
zs_log = f'[log]zs_{time.strftime("%Y%m%d_%H%M%S")}.log'

def setup_logger(logfile):
    logger = logging.getLogger()
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')

        file_handler = logging.FileHandler(logfile,'a','utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

def mc_message(message, logfile=mc_log):
    setup_logger(logfile)
    logging.info(message)

def zs_message(message, logfile=zs_log):
    setup_logger(logfile)
    logging.info(message)

# 清理冗余日志
def logclean(key, logfile):
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.log') and file != logfile and key in file:
                os.remove(os.path.join(root, file))
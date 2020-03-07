# This program demonstrate how to add multiple handler for a logger
import logging
import sys

def main():
    # get logger
    logger = logging.getLogger('myapp')

    # Define Handler for all logging information
    all_info_handler = logging.FileHandler(filename='./how2_logging/app_all_log.log', mode='a')
    # define formater for this handler
    all_info_formater = logging.Formatter(fmt='[%(asctime)s] %(levelname)s: %(message)s')
    # add formater to this handler
    all_info_handler.setFormatter(all_info_formater)
    # set the handler handling level
    all_info_handler.setLevel(logging.DEBUG)
    # add all_info_handler to logger
    logger.addHandler(all_info_handler)

    # Define Error handler here:
    critical_info_handler = logging.StreamHandler(sys.stderr)
    critical_info_formater = logging.Formatter(fmt='[%(asctime)s] %(levelname)s: %(message)s')
    critical_info_handler.setFormatter(critical_info_formater)
    critical_info_handler.setLevel(logging.ERROR)

    logger.addHandler(critical_info_handler)

    logger.info('Test message')
    logger.error('Error message')
    logger.critical('critical message')
    
if __name__ == "__main__":
    main()
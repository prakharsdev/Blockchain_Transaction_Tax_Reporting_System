import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

# Example usage
if __name__ == '__main__':
    logger = setup_logging()
    logger.info('This is an info message')

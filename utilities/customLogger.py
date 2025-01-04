import logging

class LogGen:
    @staticmethod
    def log():
        logging.basicConfig(filename=r".\logs\automation.log", format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
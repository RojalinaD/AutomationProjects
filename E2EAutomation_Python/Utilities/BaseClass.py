import inspect
import logging

import pytest



@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        print("Hi", loggername)
        logger = logging.getLogger(loggername)
        print("Bye", logger)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.debug("This is the DEBUG part")
        logger.info("This is the INFO part")
        logger.warning("There is some warning")
        logger.critical("There is a critical error")
        logger.setLevel(logging.WARNING)


        return logger

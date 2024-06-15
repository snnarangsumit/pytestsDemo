import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger



#The line of code loggerName = inspect.stack()[1][3]
# is used to dynamically retrieve the name of the calling function within a Python script.
# This is particularly useful in logging where you might want to automatically
# include the name of the function that generated a log entry.
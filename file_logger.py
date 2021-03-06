from logger import logger

class file_logger:

    """
    Constructor
    """
    # check if we get file name
    def __init__(self, log_level, file_name = 'file_log'):
        self.__log_level__ = log_level
        self._file_= open(file_name + '.txt', 'a+')


    """
    log
    Logs the message if log_level is less than or equal to
    the class' threshold. (In this case: does nothing.)
    """
    def log(self, log_level, message):
        if log_level <= self.__log_level__:
            self._file_.write(str(log_level) + ': ' + message + '\n')


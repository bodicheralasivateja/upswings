import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        log_file = os.path.join(r"C:\Users\Lenovo\PycharmProjects\pythonProject\upswings\Logs", "automation.log")

        if not os.path.exists(os.path.dirname(log_file)):
            os.makedirs(os.path.dirname(log_file))

        fhandler = logging.FileHandler(filename=log_file, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)

        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)

        return logger

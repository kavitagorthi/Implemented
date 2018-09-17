#simple.py
import logging
from datetime import date

format1 = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"

format2 = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"
formatter2 = logging.Formatter(format2)
file_handler = logging.FileHandler(str(date.today()) + ".log")
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter2)



formatter = logging.Formatter(format1)
file_handler = logging.FileHandler('mylog.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(100)
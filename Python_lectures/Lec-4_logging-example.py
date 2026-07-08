import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

def fun1(n):
    if n < 0:
        raise ValueError("Value entered is less than zero")
    else:
        logger.info("Operation performed successfully!")


try:
    n = int(input("Enter a number:"))
    fun1(n)
except ValueError as e:
    logging.exception("Exception occured %s",str(e))


# from loguru import logger

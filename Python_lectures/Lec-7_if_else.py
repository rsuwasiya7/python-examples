import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()


length = int(input("Enter the length's value : "))

if length <= 100:
    logger.info("Your Length is not sufficient for 4 BHK.")
    if length > 80:
        logger.info("You can go ahead with 3BHK")
    else:
        logger.info("Sorry no space for the project.")
elif length > 500:
    logger.info("2 buildings can be created with given length.")
else:
    logger.info("Your Design will be created.")

# Even or ODD

number = int(input("Enter a number :"))

if number%2 == 0:
    logger.info(f"{number} is even number.")
else:
    logger.info(f"{number} is odd number.")
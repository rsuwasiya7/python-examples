print("Python Basics\nNew Line created")
print('''Test 1
      Test2''')

print("Test \"double quotes\" now!")
print('Test "double quotes" now 2!')

cost = 100
cost2 = 200

print(f"Cost of item is {cost}")

print("Cost of item2 and item1 is {1} and {0} respectively".format(cost, cost2))


import logging
logger = logging.getLogger("simple logger")
logger.setLevel(logging.DEBUG)



file_handler = logging.FileHandler("app.log")
logger.addHandler(file_handler)
logger.info("Test1")
logger.info("This is an info message")
logger.error("This is an error message")

# logger1 = logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
# logger1.info("Test2")

logging.basicConfig(level=logging.INFO)
logger1 = logging.getLogger()
age = 25
logger1.info("The value of age is %d", age)
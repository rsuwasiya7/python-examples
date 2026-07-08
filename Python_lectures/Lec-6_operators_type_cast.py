# operator, type casting and user input in python
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()
import math

a = -101
b = 10

logger.info(f"Add= {a+b}")
logger.info(f"Sub= {a-b}")
logger.info(f"Multi= {a*b}")
logger.info(f"Div= {a/b}")
logger.info(f"Mod= {a%b}")
logger.info(f"Floor= {a//b}")

a = 17
b = 6
logger.info(f"Div= {a/b}")
logger.info(f"Floor= {a//b}")
logger.info(f"Ceil = {math.ceil(a/b)}")

var1 = "abc1"
var2 = "xyz2"

logger.info(f"Concat = {var1+var2}")

# Type casting

val1 = "100"
val2 = 200

logger.info(f"Add 2 vals = {int(val1) + val2}")

a = 10.5
b = 3

logger.info(f"a is {type(a)} and value is {a}")
logger.info(f"a is {type(b)} and value is {b}")
logger.info(f"a+b type is {type(a+b)} and val is {a+b}")

length = input("Enter the value of length:")
breadth = input("Enter the value of breadth:")
logger.info(f"Area = {int(length)*float(breadth)}")


logger.info(f"Area absolute = {abs(int(length)*float(breadth))}")
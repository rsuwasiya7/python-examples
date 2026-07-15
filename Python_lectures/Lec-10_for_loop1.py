import logging

# Configure the root logger: set the threshold to INFO and customize the output format 
# to display the log level, file name, line number, and the actual message.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

# List of worker names to iterate through
labour_names = ["Mahesh", "Ramesh", "Sumesh", "Naresh", "Himesh"]

# Loop 1: Iterate directly through the list items to log attendance
for name in labour_names:
    logger.info(f"Labour {name} is present.")

# Loop 2: Iterate using indices to log both the 1-based position and the corresponding name
for i in range(len(labour_names)):
    logger.info(f"Labour{i+1}'s name is {labour_names[i]}.")

# Pattern 1: Print an increasing triangle pattern of stars using a 1-to-5 range
for i in range(1, 6):
    print(i * "* ")

# Pattern 1 (Alternative): Achieve the same increasing triangle by shifting a 0-to-4 range by 1
# Another way
for i in range(5):
    print((i+1) * "* ")

# Pattern 2: Print a decreasing triangle pattern of stars by counting backward from 5 down to 1
for i in range(5, 0, -1):
    print(i * "* ")

# Even Numbers - Method 1: Check every number from 0 to 100 using the modulo operator (%)
print("Even number till 100 are : ", end='')
for i in range(101):
    if i % 2 == 0:  # If divisible by 2 with no remainder, it's even
        print(i, end=' ')

# Even Numbers - Method 2: Optimize by skipping numbers, stepping by 2 directly from 0
print("\n2nd method : Even number till 100 are : ", end='')
for i in range(0, 101, 2):  # Starts at 0, goes up to 100, jumps by 2
    print(i, end=' ')

# Odd Numbers - Method 1: Check every number from 0 to 100 using the modulo operator (%)
print("\nODD number till 100 are : ", end='')
for i in range(101):
    if i % 2 != 0:  # If divided by 2 leaves a remainder, it's odd
        print(i, end=' ')

# Odd Numbers - Method 2: Optimize by skipping numbers, stepping by 2 directly from 1
print("\n2nd method : ODD number till 100 are : ", end='')
for i in range(1, 101, 2):  # Starts at 1, goes up to 99, jumps by 2
    print(i, end=' ')
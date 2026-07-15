import logging
import time

# Configure the root logger: set the threshold to INFO and customize the output format 
# to display the log level, file name, line number, and the actual message.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

# List of worker names to iterate through
labour_names = ["Mahesh", "Ramesh", "Sumesh", "Naresh", "Himesh"]

# --- Logic 1: Ascending Iteration using a standard while loop ---

# Initialize a counter index variable at 0 (the first element of the list)
i = 0

# Loop runs as long as the counter is strictly less than the total count of names (5)
while i < len(labour_names):
    # Log the human-readable index (1-based, i+1) and look up the string name at index `i`
    logger.info(f"labour {i+1} is {labour_names[i]}")
    # CRITICAL: Manually increment the index by 1 to move to the next item and prevent an infinite loop
    i += 1

print("Logic 2 in descending:")

# --- Logic 2: Descending Iteration using a backward counting while loop ---

# Track the length of the list (initial value is 5)
n = len(labour_names)

# Loop runs backward down to 0. Since list indexing is 0-based, the final target 
# boundary condition is index 0, which corresponds to (n - 1) == 0.
while (n - 1) >= 0:
    # Log the current 1-based number position (`n`) and look up the array element at `n - 1`.
    # First iteration looks up index 4 (Himesh), down to index 0 (Mahesh).
    logger.info(f"labour {n} is {labour_names[n - 1]}")
    
    # Introduce an artificial execution pause of 3 seconds between iterations
    time.sleep(3)
    
    # CRITICAL: Decrement the length counter by 1 to move backward through the list structures
    n -= 1
import logging

# Configure the root logger: set the threshold to INFO and customize the output format 
# to display the log level, file name, line number, and the actual message.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

# Initialize a base dictionary with name strings as keys and cost integers as values
labours_with_cost = {"Mahesh" : 500, "Mithilesh": 400, "Ramesh" : 600, "Sumesh" : 700, "Naresh":1000, "Himesh":1200}
logger.info(labours_with_cost)

# Safe Retrieval: .get() returns the value if the key exists
logger.info(labours_with_cost.get("Mahesh"))

# Case Sensitivity: "mahesh" (lowercase) doesn't exist. .get() safely handles this by returning None
logger.info(labours_with_cost.get("mahesh")) # gives None

# Bracket Hazard (Commented out): Direct bracket lookups on non-existent keys crash the program with a KeyError
# logger.info(labours_with_cost["mahesh"]) #KeyError

# View Objects: Extract structural components of the dictionary (these dynamically reflect changes)
logger.info(labours_with_cost.keys())   # Returns a view object of all keys
logger.info(labours_with_cost.values()) # Returns a view object of all values
logger.info(labours_with_cost.items())  # Returns a view object of all (key, value) tuple pairs

# Multi-record modification: Use .update() to add new key-value pairs or overwrite existing ones in-place
labours_with_cost.update({"Manish":600, "Vinish": 800})
logger.info(labours_with_cost)

# Dictionary Merging: Use the double-asterisk (** ) operator to unpack multiple dictionaries into a brand-new one
new_dict = {"Manish":600, "Vinish": 800}
final_dict = {**labours_with_cost, **new_dict}
logger.info(final_dict)

# Element Removal:
print(final_dict.pop("Vinish")) # Removes the specific key "Vinish" and returns its associated value (800)
print(final_dict.popitem())     # Removes and returns the last inserted (key, value) tuple (LIFO order)
logger.info(final_dict)

# Memory Copies: Use .copy() to make a shallow copy of the dictionary at a completely different memory location
new_labour = final_dict.copy()
# id() verifies that these two variables point to distinct objects in memory
logger.info(f"{new_labour} saved at {id(new_labour)}")
logger.info(f"{final_dict} saved at {id(final_dict)}")

# Resetting: Completely wipe out all elements from the copied dictionary, leaving it empty ({})
new_labour.clear()
logger.info(f"{new_labour}")

# --- Value Updates: Comprehension vs Loops ---

# Method A: Dictionary comprehension looping over raw keys, accessing old values via brackets
labours_with_cost = {key:labours_with_cost[key]+100 for key in labours_with_cost}
logger.info(f"New salary :  {labours_with_cost}")

# Method B: Dictionary comprehension looping cleanly over unpackable key-value pairs (.items())
labours_with_cost = {key:value+100 for key,value in labours_with_cost.items()}
logger.info(f"New salary :  {labours_with_cost}")

# Method C: Conditional comprehension applying changes exclusively to values that match a specific criteria (< 1000)
labours_with_cost = {key:(value+100 if value<1000 else value) for key,value in labours_with_cost.items()}
logger.info(f"New salary :  {labours_with_cost}")

# Method D: Standard loop modifying values directly in-place without generating a whole new dictionary object
for key in labours_with_cost:
    # Check the condition, and only update if it matches
    if labours_with_cost[key] < 1000:
        labours_with_cost[key] += 100

logger.info(f"New salary :  {labours_with_cost}")
logger.info(f"Length : {len(labours_with_cost)}") # Read total element count


# --- Frequency Distribution Practice ---

name = "Nikola Tesla"
char_count = {}

# String iteration: Loop through each individual character (including spaces) to count occurrences
for char in name:
    if char in char_count:
        char_count[char] += 1  # Increment the counter if the character has been seen before
    else:
        char_count[char] = 1   # Initialize the tracker to 1 if it's the character's first appearance

logger.info(char_count)
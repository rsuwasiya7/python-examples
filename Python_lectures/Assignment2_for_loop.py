import logging

# Configure the root logger: set the threshold to INFO and customize the output format 
# to display the log level, file name, line number, and the actual message.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

# --- Approach 1: Scan-and-Slice Insertion for an ALREADY Sorted Descending List ---

# Initial list sorted in descending order
lst = [202, 165, 89, 76, 12]
logger.info(f"list 1 in descending order: {lst}")

# Get the initial length of the list and define the number to insert
n = len(lst)
no_to_insert = 300  # Testing the critical edge case (larger than everything)
logger.info(f"New number to insert : {no_to_insert}")

# KEY ADJUSTMENT 1: Default the insertion position to the very end of the list.
# If the number is smaller than all elements, it will naturally drop at index `n`.
pos_to_insert = n

# Loop through the list to find where the descending pattern breaks for our new number.
for i in range(n):
    # KEY ADJUSTMENT 2: The exact moment we find an element smaller than our new number,
    # we have found its correct index position. 
    if no_to_insert > lst[i]:
        pos_to_insert = i
        break  # STOP scanning immediately so we don't overwrite the correct index!

# Log the determined index position where the number should be placed
logger.info(f"Index position to insert in list : {pos_to_insert}")

# Reconstruct the list by splitting it around the target index and sandwiching the new number in between
lst = lst[:pos_to_insert] + [no_to_insert] + lst[pos_to_insert:]

# Log the final updated list
logger.info(f"New list : {lst}")


# --- Approach 2: Insert and Sort via Bubble Sort for an UNSORTED List ---

# Initial unsorted list and the number we want to add to it
numbers_list = [77, 5, 200, 18, 150, 108]
new_no = 100

# 1. Insert the element at the end of the list manually using list concatenation
numbers_list = numbers_list + [new_no]
logger.info(f"Unsorted list 2 : {numbers_list}")

# 2. Sort the entire updated list into descending order using custom Bubble Sort logic
n = len(numbers_list)

# Outer loop: Controls how many passes we make through the list
for i in range(n):
    # Optimization flag: assume the list is sorted at the start of each pass
    swapped = False
    
    # Inner loop: Pairs up adjacent elements, shrinking the comparison range as large numbers settle
    for j in range(0, n - i - 1):
        # Check if the left number is SMALLER than the right number.
        # If it is, they are out of order for a descending list.
        if numbers_list[j] < numbers_list[j + 1]:
            # Swap their physical positions in the list without built-in functions
            numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
            # Mark that a swap occurred, meaning the list wasn't fully sorted yet
            swapped = True
            
    # Optimization check: If a full pass happens without a single swap, the list is perfectly sorted. 
    # We break early to save CPU processing time.
    if not swapped:
        break

# Print the final output to the console
print(numbers_list)
logger.info(f"New sorted list in descending order:: {numbers_list}")
# Output: [200, 150, 108, 100, 77, 18, 5]

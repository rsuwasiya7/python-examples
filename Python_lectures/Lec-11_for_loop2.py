import logging

# Configure the root logger: set the threshold to INFO and customize the output format 
# to display the log level, file name, line number, and the actual message.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

# Long multi-line text paragraph used for text processing/word counting
paragraph = """Python is uniquely suited for data engineering because its foundational design aligns perfectly with high-volume data architecture. 
One of its most powerful "under the hood" secrets is its extensive use of iterators and generators, which allow data engineers to stream and process massive datasets 
lazily—one record at a time—without overwhelming system memory. This object-oriented flexibility is paired with a C-based backbone, meaning heavy-lifter libraries like Pandas 
and NumPy act as fast wrappers over highly optimized compiled code. Additionally, Python treats functions as first-class citizens, a feature that seamlessly translates to 
functional programming paradigms. This specific capability directly mirrors the distributed data transformation logic used by massive cluster-computing frameworks like 
Apache Spark, making the transition from writing a local Python script to orchestrating a multi-node PySpark workflow completely natural."""

# --- Part 1: Word Counting Logic ---

# Standardize the text: convert everything to lowercase to make the match case-insensitive,
# then split the string into a list of words using space as a delimiter.
list_words = paragraph.lower().split(" ")
print(list_words)

# Initialize a counter variable to keep track of matches
count = 0

# Iterate through the list of words and increment the counter every time "python" is found
for word in list_words:
    if word == "python":
        count += 1

# Log the final frequency result
logger.info(f"Total no. of occurances of 'Python' is {count}.")


# --- Part 2: Inserting into an ALREADY Sorted Ascending List (Handling Duplicates) ---

# Initial sorted list in ascending order
numbers_list = [5, 18, 77, 108, 150, 200]
new_no = 77  # Testing a duplicate item edge case (77 is already at index 2)
print(numbers_list)

# Track the targeted location where the item should sit
index = 0

# Loop through the list to scan for the correct placement boundary
for i in range(len(numbers_list)):
    # Keep moving right as long as the list elements are smaller than our target number.
    # When hitting a duplicate (77), 77 > 77 is False, dropping into the 'else' block immediately.
    # This places the new number directly *before* the existing duplicate.
    if new_no > numbers_list[i]:
        index += 1
    else:
        break

# Log the exact index position found
logger.info(f"New index = {index}")

# numbers_list = numbers_list + [None]
# print(numbers_list)

# for i in range(len(numbers_list)-1, index, -1):
#     if i > index:
#         numbers_list[i] = numbers_list[i-1]
#         print(numbers_list)

# numbers_list[index] = new_no

# [Commented Code Block Explanation]:
# The commented section above demonstrates an "in-place shift" alternative.
# It works by tacking [None] onto the end to expand the list space, looping backward 
# from the right, shifting everything right by 1 spot until it hits the target index,
# and then overwriting that specific index slot with the new number.

# Slicing Method: Reconstruct the list cleanly by carving it at our tracked index,
# adding the new element, and joining the tail end back together.
numbers_list = numbers_list[:index] + [new_no] + numbers_list[index:]
print(numbers_list)


# --- Part 3: Insert and Sort via Bubble Sort (Ascending Order) ---

# An unsorted list and the number we want to incorporate into it
new_list = [100, 200, 10, 7, 20, 130]
new_num = 171

# Step 1: Append the element blindly to the end of the list using list concatenation
new_list = new_list + [new_num]
n = len(new_list)

# Step 2: Sort the entire updated list into ascending order using custom Bubble Sort logic
for i in range(n):
    # Optimization flag: assume the list is sorted at the start of each pass
    swapped = False
    
    # Inner loop: Pairs up adjacent elements, shrinking the comparison window as large values bubble up
    for j in range(0, n - i - 1):
        # ASCENDING CRITERIA: Check if the left number is GREATER than the right number.
        # If it is, they are out of order for an ascending list.
        if new_list[j] > new_list[j + 1]:
            # Swap their physical positions in the list without built-in helper tools
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
            # Mark that a swap occurred, meaning the list wasn't fully sorted yet
            swapped = True

    # Optimization check: If a full pass happens without a single swap, the list is perfectly sorted.
    # Break early to prevent redundant loop cycles.
    if not swapped:
        break

# Print the final cleanly ordered result to the console
print(f"New sorted list in ascending order:: {new_list}")

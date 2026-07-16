import logging

# Configure the root logger: set the threshold to INFO and customize the output format 
# to display the log level, file name, line number, and the actual message.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

# --- Part 1: Basic Filtering (Traditional Loop vs List Comprehension) ---

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []

# Traditional Approach: Loop through the list, check the condition, and manually append matches
for n in number_list:
    if n % 2 == 0:  # Check if the number is divisible by 2 with no remainder
        even_list.append(n)
logger.info(f"New even list : {even_list}")

# List Comprehension Alternative: Clean filtering layout [expression for item in iterable if condition]
even_list2 = [n for n in number_list if n % 2 == 0]
logger.info(f"New even list : {even_list2}")


# --- Part 2: Conditional Transformation (Traditional Loop vs List Comprehension) ---

new_list = []

# Traditional Approach: Loop through numbers and apply if-else blocks to append different strings
for n in number_list:
    if n % 2 == 0:
        new_list.append("Even")
    else:
        new_list.append("Odd")
logger.info(f"New even,odd list : {new_list}")

# List Comprehension Alternative using inline IF-ELSE: [true_expr if condition else false_expr for item in iterable]
# Note: This implementation generates values dynamically across the range 1 to 10
new_list2 = ["Even" if n % 2 == 0 else "Odd" for n in range(1, 11)]
logger.info(f"New even,odd list : {new_list2}")


# --- Part 3: Data Cleansing & Text Standardisation ---

raw_names = ["mahesh", "RAMESH", "suMesh ", "naresh", "himesh"]

# Standardise messy user input strings: remove trailing spaces (.strip()) and capitalize properly (.title())
standard_names = [n.strip().title() for n in raw_names]
logger.info(f"Standard names : {standard_names}")


# --- Part 4: Data Threshold Filtering ---

sensor_readings = [72, -5, 68, 0, 75, -12, 80]

# Extract only positive telemetry data points, dropping negative readings and zeroes completely
correct_readings = [n for n in sensor_readings if n > 0]  
logger.info(f"Correct readings : {correct_readings}")


# --- Part 5: Data Flagging / Categorisation ---

weekly_hours = [38, 45, 40, 48, 35]

# Generate status strings based on numeric values to flags anomalies or payroll statuses
work = ["Overtime" if n > 40 else "Standard" for n in weekly_hours]
logger.info(f"Work data : {work}")


# --- Part 6: Missing Value Elimination & Type Casting ---

raw_readings = ["23.5", None, "71.2", 45, None, "18.9", 0]

# Multi-step cleaning: The right-side filter (if n is not None) fires first to drop invalid entries,
# then the remaining integers and strings are normalized into floating-point numbers on the left.
clean_readings = [float(n) for n in raw_readings if n is not None]
logger.info(f"Clean readings : {clean_readings}")

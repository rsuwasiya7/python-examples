import logging

# Configure the root logger: set the threshold to INFO and customize the output format 
# to display the log level, file name, line number, and the actual message.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

def calculation(a, b, operand):
    # Core operational function handling type conversions and calculations
    try:
        if operand == '+':
            return float(a) + float(b)
        elif operand == '-':
            return float(a) - float(b)
        elif operand == '*':
            return float(a) * float(b)
        elif operand == '/':
            # Edge Case: Prevent crash if user tries to divide by zero
            if float(b) == 0:
                logger.error("Division by zero error!")
                return None
            return float(a) / float(b)
        else:
            print("Invalid operator! Select +, -, *, or /")
            return None
    except ValueError:
        logger.error("Invalid number input provided.")
        return None

# Get initial inputs to start the calculation engine
a = input("Enter the first number: ")
operand = input("Select '+' for Addition, '-' for Subtraction, '*' for Multiplication, '/' for Division : ")
b = input("Enter another number: ")

# Run the first calculation outside the loop to establish our baseline running total
current_result = calculation(a, b, operand)

while True:
    # If a calculation error occurred (like invalid operator or division by zero), handle it safely
    if current_result is None:
        print("Calculation failed. Please restart.")
        break
        
    print(f"Current Running Total = {current_result}")
    
    # Prompt user for the next operational choice
    next_action = input("Select '=' for final result, or enter the next operator (+, -, *, /): ")
    
    if next_action == '=':
        print(f"🏆 Final result = {current_result}")
        break
    
    # If the user did not say '=', then the input must be treated as the new operator
    operand = next_action
    
    # Get the next number to apply to our running total
    next_num = input("Enter the next number: ")
    
    # Update our running total by shifting the current result into the 'a' parameter position
    current_result = calculation(current_result, next_num, operand)
import logging

# Configure the root logger: set the threshold to INFO and customize the output format 
# to display the log level, file name, line number, and the actual message.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

labours_with_cost = {"Mahesh" : 500, "Mithilesh": 400, "Ramesh" : 600, "Sumesh" : 700, "Naresh":1000, "Himesh":1200}
logger.info(labours_with_cost)

total_cost = 0

for name, daily_rate in labours_with_cost.items():
    # 1. Determine the days worked based on the specific person
    if name == "Mahesh":
        days_worked = 48
    elif name == "Naresh":
        days_worked = 45
    else:
        days_worked = 50
        
    # 2. Calculate the individual cost and add it to our running total
    worker_total = daily_rate * days_worked
    total_cost += worker_total
    
    # Optional logging to trace the data pipeline math step-by-step
    logger.info(f"{name} worked {days_worked} days at {daily_rate}/day = {worker_total}")

print("-" * 30)
print(f"Grand Total Cost: {total_cost}")

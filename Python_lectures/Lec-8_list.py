import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

labour_names = ["Mahesh","Ramesh","Sumesh","Naresh","Himesh"]
logger.info(f"List of labours is : {labour_names}")

logger.info(f"First element in list of labours is {labour_names[0]}")
logger.info(f"Last element in list of labours is {labour_names[-1]}")

labour_names.append("Vinesh")
logger.info(f"New Last element in list of labours is {labour_names[-1]}")

new_labours = ["Ram","Shyam"]
labour_names.extend(new_labours)
labour_names.insert(0,"Aam")
logger.info(f"New list of labours is : {labour_names}")

foreign_labours = ["Ford","Henry","Max"]
labour_names = foreign_labours + labour_names
logger.info(f"New list of labours with Foreigners is : {labour_names}")


# for i in range(len(labour_names)):
#     logger.info(f"For {i} memory - {id(labour_names)}")


# Multi-dim Lists

labours_with_pay = [["Ram", 1000], ["Shyam", 700], ["Aam", 500], ["Jaggu", 300]]

logger.info(f"Pay of {labours_with_pay[0][0]} is {labours_with_pay[0][1]}")

# for i in range(len(labours_with_pay)):
#     for j in range(len(labours_with_pay[i])):
#         logger.info(f"Pay of {labours_with_pay[i][j]} is {labours_with_pay[i][j]}")
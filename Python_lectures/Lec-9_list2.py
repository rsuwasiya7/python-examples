import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

list1 = [1,2,2,2,3,3,3,3,4,4,5,5,5,5,5]
list2 = [10, "Rahul", "Manish", 10.57]
labour_names = ["Mahesh","Ramesh","Sumesh","Naresh","Himesh"]
new_labours = ["Ram","Shyam"]
foreign_labours = ["Ford","Henry","Max"]

# Add multiple lists
labour_names = foreign_labours + new_labours + labour_names
logger.info(f" Original labot names list : {labour_names}")

# Display from 2nd element
logger.info(labour_names[1:])

# Display from 2nd element to 5th element
logger.info(labour_names[1:5])

# It will return empty list if out of range slicing is given
logger.info(labour_names[15:])

# will print the last element (will give same result -> labour_names[-1])
logger.info(labour_names[-1:])

# Reverse the list
logger.info(labour_names[::-1])

# Length of list
logger.info(f"Length of list : {len(labour_names)}")

# Insert at 4th element
labour_names.insert(3,"Stuart")
logger.info(f"New list : {labour_names}")
logger.info(f"Length of list : {len(labour_names)}")

# Insert at the end
labour_names.append("Dinesh")
logger.info(f"New list : {labour_names}")
logger.info(f"Length of list : {len(labour_names)}")

# Remove element from the end
logger.info(f"Removed element : {labour_names.pop()}")
logger.info(f"New list : {labour_names}")
logger.info(f"Length of list : {len(labour_names)}")

# Remove element from any particular position
logger.info(f"Removed element : {labour_names.pop(3)}")
logger.info(f"New list : {labour_names}")
logger.info(f"Length of list : {len(labour_names)}")


# Remove specific value, otherwise will throw ValueError
labour_names.remove("Sumesh")
logger.info(f"New list : {labour_names}")
logger.info(f"Length of list : {len(labour_names)}") 

# Delete existing list
del foreign_labours
# It will throw NameError: name 'foreign_labours' is not defined
# print(foreign_labours)

# Update element
labour_names[0] = "Cord"
logger.info(f"New list : {labour_names}")

# Update elements
labour_names[0:3] = ["Ford", "Fenry", "Finolex"]
logger.info(f"New list : {labour_names}")

# Sort the list
labour_names.sort()
logger.info(f"Sorted list : {labour_names}")

# Reverse Sort the list
labour_names.sort(reverse=True)
logger.info(f"Reverse list : {labour_names}")


test_sha = "2fd4e1c6-7a2d28fc-ed849ee1-bb76e739-1b93eb12"
test_sha_list = test_sha.split("-")
logger.info(test_sha_list)

api_url = "https://api.example.com/v1/posts/108/comments"
api_url_list = api_url.split("/")
logger.info(api_url_list)
logger.info(f"Post value : {api_url_list[-2]}")


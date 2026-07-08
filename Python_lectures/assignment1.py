labour_name_1st = "Mahesh"
labour_name_2nd = "Mithilesh"
labour_name_3rd = "Ramesh"
labour_name_4th = "Sumesh"
labour_wage_1st = 500
labour_wage_2nd = 400
labour_wage_3rd = 400
labour_wage_4th = 300

print(f"1st_labour_name is {labour_name_1st} and his wage is {labour_wage_1st}")
print(f"2nd_labour_name is {labour_name_2nd} and his wage is {labour_wage_2nd}")
print(f"3rd_labour_name is {labour_name_3rd} and his wage is {labour_wage_3rd}")
print(f"4th_labour_name is {labour_name_4th} and his wage is {labour_wage_4th}")

para_print = "\"\"\" Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that\n    we are implemeting all the logics by ourself. The aim here is to build our \"4 BHK\" house with the \n    help of 'Python programming'. We have total land is of \\100 ft * 100ft /, to compelete the house \n    we have total 6 labours with \'different skill set like \"\\\\ building wall or building roof \\\\\".\n            I have to print this paragraph as it is given here.\"\"\" "

print(para_print)

import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()

logger.info(f"labour_wage_1st = {id(labour_wage_1st)} \nlabour_wage_2nd = {id(labour_wage_2nd)} \nlabour_wage_3rd = {id(labour_wage_3rd)} \nlabour_wage_4th = {id(labour_wage_4th)}")

print(f"{id(labour_wage_1st)} , {id(labour_wage_2nd)} , labour_wage_3rd = {id(labour_wage_3rd)}, labour_wage_4th = {id(labour_wage_4th)}")
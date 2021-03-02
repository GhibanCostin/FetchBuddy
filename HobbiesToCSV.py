import csv
import pandas as pd
from random import seed
from random import randint

def createDictFromCSV(file):
    my_dict = {}

    data = pd.read_csv(file)
    for i in range(len(data.values)):
        my_dict[data.values[i][0]] = data.values[i][1]

    return my_dict


file1 = open('hobbies.txt', 'r')
lines = file1.readlines()

seed(1)

hob_id = createDictFromCSV('hobbies.csv')
hob_len = len(hob_id)
dep_id = createDictFromCSV('department.csv')
dep_len = len(dep_id)

hob_keys = list(hob_id.keys())
hob_values = list(hob_id.values())

dep_keys = list(dep_id.keys())
dep_values = list(dep_id.values())

with open('EmployeeData.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='\n', quoting=csv.QUOTE_MINIMAL)

    spamwriter.writerow(['Employee_Id', 'Name', 'Department', 'Project', 'Hobby'])

    for i in range(len(lines)):
        rand_hob = randint(0, hob_len - 1)
        rand_dep = randint(0, dep_len - 1)
        rand_proj = randint(1, 13)

        # print(hob_keys[hob_values.index(rand_hob)])

        spamwriter.writerow([i, lines[i][:-1], dep_keys[dep_values.index(rand_dep)], rand_proj, hob_keys[hob_values.index(rand_hob)]])
        # spamwriter.writerow([i, lines[i][:-4], rand_dep, rand_proj, rand_hob])


hobby_to_index = {}

customer_data = pd.read_csv('department.csv')
for i in range(len(customer_data.values)):
    hobby_to_index[customer_data.values[i][0]] = customer_data.values[i][1]




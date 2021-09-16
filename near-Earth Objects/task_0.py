import csv
import os
import json

path = os.getcwd()

file =  path + '/project/data/neos.csv'
cnter= 0
cnter_names = 0
cnter_diame = 0

with open(file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    print(type(reader))

    for row in reader:
       if cnter == 0 :
           pd_1 = row[3]

       if row[4] == 'Apollo':
           diameter = row[15]

       if row[4] != '':
           cnter_names+=1

       if row[15] != '':
           cnter_diame += 1

       cnter += 1


print('# How many NEOs are in the neos.csv data set? {}'.format(cnter))
print('What is the primary designation of the first Near Earth Object in the neos.csv data set? {}'.format(pd_1))
print('What is the diameter (in kilometers) of the NEO whose name is "Apollo"? {}'.format(diameter))
print('How many NEOs have IAU names in the data set? {}'.format(cnter_names))
print('How many NEOs have diameters in the dataset {}'.format(cnter_diame))


# Using DictReader
print('--------')

cnter = 0
cnter_names = 0
cnter_diame = 0

with open(file, 'r') as csv_file:
    dict_reader = csv.DictReader(csv_file)
    print(type(dict_reader))

    for elem in dict_reader:
        if cnter == 0 :
            pd_1 = elem['diameter']
        if elem['name'] == 'Apollo':
            diameter = elem['diameter']
        if elem['name'] != '':
            cnter_names+=1

        if elem['diameter'] != '':
            cnter_diame += 1

        cnter += 1

        if cnter == 4:
            print(elem)

print('How many NEOs are in the neos.csv data set? {}'.format(cnter))
print('What is the primary designation of the first Near Earth Object in the neos.csv data set? {}'.format(pd_1))
print('What is the diameter (in kilometers) of the NEO whose name is "Apollo"? {}'.format(diameter))
print('How many NEOs have IAU names in the data set? {}'.format(cnter_names))
print('How many NEOs have diameters in the dataset {}'.format(cnter_diame))

# Open a json file
json_file = '/Users/wendy/Documents/training/Intermediate_Python/project/data/cad.json' # path + '/project/data/cad.json`'

with open(json_file) as jfile:
    jsonStr = json.load(jfile)
    print(type(jfile))

cadData = jsonStr['data']
resp2 = ''
resp3 = ''
resp4 = []

for neo in cadData:
    dateD = neo[3].split()

    if dateD[0] == '2000-Jan-01' and neo[0] == '2015 CL':
        resp2 = neo[5]

    if dateD[0] == '2000-Jan-01' and neo[0] == '2002 PB':
        resp3 = neo[7]

    if neo[0] == '170903':
        print('find several rows with this primary designation {}'.format(neo[0]))
        resp4 = neo
        print(neo)

print('How many close approaches are in the cad.json data set? {}'.format(jsonStr['count']))
print('On January 1st, 2000, how close did the NEO whose primary designation is "2015 CL" pass by Earth? {}'.format(resp2))
print('On January 1st, 2000, how fast did the NEO whose primary designation is "2002 PB" pass by Earth? {}'.format(resp3))

# Uses Heath Nutrition and Population statistics,
# stored in the file HNP_Data.csv.gz,
# assumed to be located in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
import gzip
from collections import defaultdict

def is_truncate(num):
    l = str(num).split(("."))
    left = l[0]
    right = l[1]
    if(right == "0"):
        return int(left)
    else:
        return num




filename = 'HNP_Data.csv.gz'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None
#countries_for_max_value_per_year = {}

countries_for_max_value_per_year = defaultdict(list)
maxvalue = float("-inf")

with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)

    rows = [row for row in file]
    column = rows[0]

    for i in rows:
        if (len(i) >= 3):
            if i[2].strip() == indicator_of_interest.strip():
                for j in range(4, len(i)):
                    if (not i[j] == ""):
                        maxvalue = max(maxvalue, float(i[j]))

    for i in rows:
        if (len(i) >= 3):
            if i[2].strip() == indicator_of_interest.strip():
                for j in range(4, len(i)):
                    if (not i[j] == ""):
                        if (float(i[j]) == maxvalue):
                            countries_for_max_value_per_year[rows[0][j]].append(i[0])
'''
                            if(rows[0][j] not in countries_for_max_value_per_year):
                                countries_for_max_value_per_year[rows[0][j]] = [i[0]]
                            else:
                                countries_for_max_value_per_year[rows[0][j]].append([i[0]])
'''

if (maxvalue != float("-inf")):
    max_value = is_truncate(maxvalue)

if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                    for year in sorted(countries_for_max_value_per_year)
                    )
          )


# csv_reader.py
# This program reads in data from a csv file and outputs each line as a list
# Author: Zoe McNamara Harlowe

import csv

FILENAME = "data.csv"
DATADIR = "../../pfda-mywork/"

with open(DATADIR + FILENAME, "rt") as f:
    csv_reader = csv.reader(f, delimiter = ",")

    linecount = 0

    for line in csv_reader:
        if not linecount: 
            print(f"{line}\n--------------------") # separates header from data
        else:
            print(line) # all subsequent lines
        linecount += 1

    # Calculate average age
    f.seek(0) # reset file read position to start of file

    linecount = 0
    total = 0
    
    for line in csv_reader:
        if not linecount: 
            pass
        else:
            total += int(line[1]) # ages is in second column
        linecount += 1

    print (f"Average age is {total/(linecount-1)} years old") # average age, excluding header









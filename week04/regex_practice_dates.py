# This script reads a log file line by line and uses a regular expression to find and print text enclosed in square brackets.
# regex_practice_dates.py
# Author: Zoe McNamara Harlowe

import re


regex = r"\[.*\]" # Regular expression to find text within square brackets
filename = "smaller_access.log"

# Open file
with open(filename) as input_file:
    for line in input_file:
        found_text_list = re.findall(regex, line) # Find all occurrences of the regex pattern in the line
        if (len(found_text_list) != 0): # If something is found, print it
            print(found_text_list)
            found_text = found_text_list[0] # Get the first found text
            print(found_text)
            # If I did not want the [] at the beginning and end:
            print(found_text[1:-1]) # Print the found text without the square brackets
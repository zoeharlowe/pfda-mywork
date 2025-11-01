# ip_anon.py
# This program will anonymise the sub domains of IP addresses in a log file
# by replacing the last two triplets with 'XXX'
# The new lines are stored in another file
# Author: Zoe McNamara Harlowe


## This didn't work



import re
#regex = "\d{1,3}\.\d{1,3} " # this will find other numbers apart from ips
regex =r"(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}" # we make a group at the eginning to keep
replacementText="\\1XXX.XXX " # note the space at the end to match above
filename = "smaller_access.log"
outputFileName = "anonymisedIPs.txt"


with open(filename) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
        # for debugging
        #foundText = re.search(regex, line).group()
        #print(foundText)
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)
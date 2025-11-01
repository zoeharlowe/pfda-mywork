# regex_practice.py 
# This code will find some text in an access file
# Author: Zoe McNamara Harlowe

import re

# Another example - find all URLs
filename = "smaller_access.log"
regex_url = "https?://\S+"

# Open file
with open(filename) as input_file:
    for line in input_file:
        found_url_list = re.findall(regex_url, line) # Find all occurrences of the regex pattern in the line
        if (len(found_url_list)) != 0:
            print(found_url_list)
            found_urls = found_url_list[0]
            print(found_urls)
        

        
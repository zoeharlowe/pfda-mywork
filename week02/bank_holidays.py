# bank_holidays.py
# This program will print a JSON file of UK bank holidays
# Author: Zoe McNamara Harlowe

import requests
import json

url="https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data['northern-ireland']['events'][0]) # prints first event in Northern Ireland bank holidays
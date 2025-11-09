# apollo_launch_duration.py
# Calculating how much time has passed from the Apollo 11 launch in 1969 to right now 
# Author: Zoe McNamara Harlowe

import datetime
import pytz

current_date = datetime.datetime.now()
launch_date = datetime.datetime(1969, 7, 16, 9, 32)
duration = current_date - launch_date

duration_in_s = duration.total_seconds()
years = divmod(duration_in_s, 31536000)[0]  # Seconds in a year=365*24*60*60 = 31536000
days  = divmod(duration_in_s, 86400)[0]     # Seconds in a day = 86400
hours = divmod(duration_in_s, 3600)[0]      # Seconds in an hour = 3600
minutes = divmod(duration_in_s, 60)[0]      # Seconds in a minute = 60

print(f"Number of Years:   {years}")
print(f"Number of Weeks:   {days/7}")
print(f"Number of Days:    {days}")
print(f"Number of Hours:   {hours}")
print(f"Number of Minutes: {minutes}")
print(f"Number of Seconds: {duration_in_s}")
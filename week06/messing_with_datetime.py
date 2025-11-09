# messing_with_datetime.py
# Messing around with the datetime module
# Author: Zoe McNamara Harlowe

# Breakout 4
# Write a function (named number_days_between) that:
# Takes two arguments that are 8-digit integers of the form YYYYMMDD (actually a date), and
# Returns the number of days between the two dates.

import datetime as dt

def number_days_between(date1, date2):
    date_format = "%Y%m%d"
    dt_date1 = dt.datetime.strptime(str(date1), date_format)
    dt_date2 = dt.datetime.strptime(str(date2), date_format)
    
    if dt_date1 < dt_date2:
        return (dt_date2-dt_date1).days
    else:
        return (dt_date1-dt_date2).days
    
print(f"{number_days_between(24431213, 20240314)} days")
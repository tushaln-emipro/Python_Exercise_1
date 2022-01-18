"""
    Program 3
    Write a Python program to calculate the number of days between two dates.
      a. Sample dates : (2014, 7, 2), (2014, 7, 11)
"""

import datetime
d0 = datetime.date(2014, 7, 2)
d1 = datetime.date(2014, 7, 11)
delta = d1 - d0
print('days :', delta.days)
print('Month :', d1.month - d0.month)
print('Year :', d1.year - d0.year)

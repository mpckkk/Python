import calendar
import datetime
import time

import square as square

print(calendar.weekheader(2))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020,9))

print(calendar.monthcalendar(2020,9))

print(calendar.calendar(2020))

day_of_the_week= calendar.weekday(3000,3,8)
print(day_of_the_week)

is_leap=calendar.isleap(2020)
print(is_leap)

how_many_leap_days=calendar.leapdays(2000,2001)
print(how_many_leap_days)

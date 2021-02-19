from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta     # timedelta is span of time

# basic timedelta
print(timedelta(days=365, hours=5, minutes=1))

# todays date
now = datetime.now()
print("today is: "+str(now))

# print todays date from one year now
print("one year from now it will be: "+str(now+timedelta(days=365)))

# timedelta with more than 1 argument
print("In 2 days and 3 weeks, it will be "+str(now+timedelta(days=2, weeks=2)))

# day 1 week ago
t = datetime.now()-timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("1 week ago it was: "+s)

# how many days in april fool
today = date.today()
uni = date(today.year, 2, 1)

if uni > today:
    print("PUCIT will be OPEN after %d days" % ((uni-today).days))
    uni = uni.replace(year=today.year)

    time_to_uni = uni-today
    print("It's just ", time_to_uni.days, "days until PUCIT opening")

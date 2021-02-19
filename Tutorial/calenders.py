import calendar

# plain calender
c=calendar.TextCalendar(calendar.MONDAY)
st=c.formatmonth(2021, 8)
print(st)

# # HTML calender
# hc=calendar.HTMLCalendar(calendar.MONDAY)
# st=hc.formatmonth(2021, 1)
# print(st)

# this feature shows zeros on the remaining places in calender 
# for i in c.itermonthdays(2021,8):
#     print(i)

# print names of days & month
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# meeting on first friday of month so we want to figure out dates
print("Teams meeting will be on: ")
for m in range(1,13):
    cal=calendar.monthcalendar(2021,m)
    week1=cal[0]
    week2=cal[1]
    if week1[calendar.FRIDAY]!=0:
       meetday=week1[calendar.FRIDAY]
    else:
        meetday=week2[calendar.FRIDAY]

    print("%10s %2d" %(calendar.month_name[m],meetday))
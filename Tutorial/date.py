from datetime import date
from datetime import time
from datetime import datetime

# todat's date
today = date.today()
print("today's date is",today)

# components of date
print("Date components:", today.day, today.month, today.year)

# today's weekday(0=mon & 6=sun)
print("Today's weekday # is:",today.weekday())
days =["mon","tue","wed","thu","fri","sat","sun"]
print("Today is:",days[today.weekday()])

## DATE OBJECT
# get date from datetime class
today=datetime.now()
print("the current date & time is :",today)

# current time
t= datetime.time(datetime.now())
print(t)


### USEFUL FORMATES ###
1      %a 	Weekday, short version          	                            Wed 	
2      %A 	Weekday, full version           	                            Wednesday 	
3      %w 	Weekday as a number 0-6, 0 is Sunday 	                        3 	
4      %d 	Day of month 01-31                  	                        31 	
5      %b 	Month name, short version 	                                    Dec 	
6      %B 	Month name, full version 	                                    December 	
7      %m 	Month as a number 01-12             	                        12 	
8      %y 	Year, short version, without century 	                        18 	
9      %Y 	Year, full version                   	                        2018 	
10     %H 	Hour 00-23                                                  	17 	
11     %I 	Hour 00-12                          	                        05 	
12     %p 	AM/PM                               	                        PM 	
13     %M 	Minute 00-59 	                         	                    41
14     %S 	Second 00-59                                                   	08 	
15     %f 	Microsecond 000000-999999                                   	548513 	
16     %z 	UTC offset                                                  	+0100 	
17     %Z 	Timezone 	                                                    CST 	
18     %j 	Day number of year 001-366                                  	365 	
19     %U 	Week number of year, Sunday as the first day of week, 00-53 	52 	
20     %W 	Week number of year, Monday as the first day of week, 00-53 	52 	
21     %c 	Local version of date and time 	                                Mon Dec 31 17:41:00 2018 	
22     %x 	Local version of date                                       	12/31/18 	
23     %X 	Local version of time                                       	17:41:00 	
24     %% 	A % character                                                  	%
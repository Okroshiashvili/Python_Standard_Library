


"""
The datetime module includes functions and classes for doing date and time parsing, formatting, and arithmetic.
"""


import datetime
import time


# Times


t = datetime.time(1, 2, 3)


print(t)
print('hour       :', t.hour)
print('minute     :', t.minute)
print('second     :', t.second)
print('microsecond:', t.microsecond)
print('tzinfo     :', t.tzinfo)


print()

print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)



# Dates


print()
print("+" * 40)


today = datetime.date.today()
print(today)

print('ctime  :', today.ctime())
tt = today.timetuple()

print('tuple  : tm_year  =', tt.tm_year)
print('         tm_month   =', tt.tm_mon)
print('         tm_mday  =', tt.tm_mday)
print('         tm_hour  =', tt.tm_hour)
print('         tm_min   =', tt.tm_min)
print('         tm_sec   =', tt.tm_sec)
print('         tm_wday  =', tt.tm_wday)
print('         tm_yday  =', tt.tm_yday)
print('         tm_isdst =', tt.tm_isdst)
print('ordinal:', today.toordinal())
print('Year   :', today.year)
print('Mon    :', today.month)
print('Day    :', today.day)



# Timedeltas


print()
print("+" * 40)


print('microseconds:', datetime.timedelta(microseconds=1))
print('milliseconds:', datetime.timedelta(milliseconds=1))
print('seconds     :', datetime.timedelta(seconds=1))
print('minutes     :', datetime.timedelta(minutes=1))
print('hours       :', datetime.timedelta(hours=1))
print('days        :', datetime.timedelta(days=1))
print('weeks       :', datetime.timedelta(weeks=1))


print("timedelta as a number of seconds")

for delta in [datetime.timedelta(microseconds=1),
              datetime.timedelta(milliseconds=1),
              datetime.timedelta(seconds=1),
              datetime.timedelta(minutes=1),
              datetime.timedelta(hours=1),
              datetime.timedelta(days=1),
              datetime.timedelta(weeks=1),
              ]:
    print('{:15} = {:8} seconds'.format(
        str(delta), delta.total_seconds())
    )




# Comparing Dates and Times


print()
print("+" * 40)


print('Times:')
t1 = datetime.time(12, 55, 0)
print('t1:', t1)
t2 = datetime.time(13, 5, 0)
print('t2:', t2)
print('t1 < t2:', t1 < t2)

print()
print('Dates:')
d1 = datetime.date.today()
print('d1:', d1)
d2 = datetime.date.today() + datetime.timedelta(days=1)
print('d2:', d2)
print('d1 > d2:', d1 > d2)




# Formatting and Parsing


print()
print("+" * 40)


format_date_time = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()
print('ISO     :', today)

s = today.strftime(format_date_time)
print('strftime:', s)

d = datetime.datetime.strptime(s, format_date_time)
print('strptime:', d.strftime(format_date_time))


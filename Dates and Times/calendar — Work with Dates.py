


"""
The calendar module implements classes for working with dates to manage year/month/week oriented values.
"""



import  calendar


# Formatting Examples

c = calendar.TextCalendar(calendar.SUNDAY)

c.prmonth(2020, 3)


print("Print calendar for year 2020")

cal = calendar.TextCalendar(calendar.MONDAY)

print(cal.formatyear(2020, 2, 1, 1, 3))


print(calendar.TextCalendar)



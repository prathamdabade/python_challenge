import datetime, calendar

for year in range(1006, 1996, 10):
  if  datetime.date(year,1,26).weekday()==0:
    if calendar.isleap(year):
      print(year)

#1756 and jan 27 -> mozart


Link : https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
  
import calendar
import datetime

month, day, year = map(int, input().split())
date = datetime.date(year, month, day)
print(calendar.day_name[date.weekday()].upper())

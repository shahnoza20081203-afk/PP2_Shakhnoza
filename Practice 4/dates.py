#1
from datetime import datetime, timedelta

current_date = datetime.now()
date_minus_5_days = current_date - timedelta(days=5)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("5 days ago:", date_minus_5_days.strftime("%Y-%m-%d"))

#2
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:    ", today)
print("Tomorrow: ", tomorrow)

#3
from datetime import datetime

dt = datetime.now()
dt_without_microseconds = dt.replace(microsecond=0)

print("With microseconds:", dt)
print("Without microseconds:", dt_without_microseconds)

#4
from datetime import datetime

date1 = datetime(2026, 9, 27, 12, 0, 0)
date2 = datetime(2026, 9, 27, 15, 30, 0)

difference = date2 - date1
difference_in_seconds = difference.total_seconds()

print(f"Difference in seconds: {int(difference_in_seconds)} seconds")


from datetime import datetime, timedelta

test_date1, test_date2 = datetime(2015, 6, 3), datetime(2015, 7, 1)

dates = (test_date1 + timedelta(idx + 1) for idx in range((test_date2 - test_date1).days))
for date in dates:
    print(date)

# summing all weekdays
res = sum(1 for day in dates if day.weekday())

# printing
print("Total business days in range : " + str(res))

from datetime import date, time, datetime

# calling the today
# function of dates class
today = date.today()
now = datetime.now()
print("Todays date is:", today)
print("\ncurrent date and time is ", now)


# printing dates components
print("\ndate components", today.year, today.month, today.day)
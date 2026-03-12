import datetime

date = datetime.date(2023, 7, 12)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
right_now_time = datetime.datetime.now()

# string format of the time
now = right_now_time.strftime("%H:%M:%S %d/%m/%Y")

print(date)
print(today)

print(time)
print(right_now_time)
print(now)

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")
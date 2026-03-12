principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))

    if principle <= 0:
        print("Principle cannot be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the rate amount: "))

    if rate <= 0:
        print("rate cannot be less than or equal to zero")
    else:
        break

while True:
    time = float(input("Enter the time amount: "))

    if time <= 0:
        print("time cannot be less than or equal to zero")
    else:
        break

total = principle * (1 + rate / 100)

print(f"Balance after {time} year/s: ${total:.2f}")
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still scheduled")

is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside.")
    print("It is sunny.")
elif temp <= 0 and is_sunny:
    print("It is cold outside and it is sunny.")
elif 28 <= temp <= 0 and is_sunny:
    print("It is warm and sunny outside.")

if not is_sunny:
    print("It is cloudy outside")
else:
    print("It is sunny outside")
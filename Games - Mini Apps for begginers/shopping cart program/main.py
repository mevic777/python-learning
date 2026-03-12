foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price for {food}: $"))    
        foods.append(food)
        prices.append(price)

for price in prices:
    total += price

print("--------------\nYour cart: \n")
for food in foods:
    print(f"{food}", end=", ")

print(f"Total: ${total}")
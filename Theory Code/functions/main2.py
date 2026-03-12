# DEFAULT parameters

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

import time 

def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("Done!")

count(30, 15)
# multithreading = Used to perform multiple task concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from API
#                  threading.Thread(target=my_function)

import threading
import time

def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking the {first}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# Here the functions are executed on only one thread
# and only one a time

# walk_dog()
# take_out_trash()
# get_mail()

# HERE THE FUNCTIONS ARE EXECUTED QUICKEST BY TIME
# SO IT IS KINDA OF MULTITASKING

# chore1 = threading.Thread(target=walk_dog, args=("Scooby")) -> args=("Scooby") - it is very important we finish it with a ','
#          so python understands that this is tuple and there are no more argumets
chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")
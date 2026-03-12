# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#              1. try, 2. except, 3. finally

try: # try the code
    number = int(input("Enter a number: "))

    print(1 / number)
except ZeroDivisionError: # handle the error
    print("You can't divide by zero")
except ValueError:
    print("You cannot divide by letters")
except Exception:
    print("Something went wrong")
finally: # executed no matter what
    print("Do some cleanup")
# variable scope = where a variable is visible
# scope resolution = Local -> Enclosed -> Global -> Build in

# Local scope
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

# Enclosed scope

def func3():
    x = 1

    def func4():
        x = 2
        print(x)
    func4()

func3()


# Global scope

def func5():
    print(x)

def func6():
    print(x)

x = 3

func5()
func6()


# Built in
import math

print(math.e)
import json, csv

file_path = "input.txt"
file_path_json = "input.json"
file_path_csv = "input.csv"


try:
    with open(file_path, "r") as file:
        content = file.read()

        print(content)

except FileNotFoundError:
    print("File is not found")

except PermissionError:
    print("You don't have access to this file")



try:
    with open(file_path_json, "r") as file:
        # content = file.read() -> both read the file
        content = json.load(file)

        # but because using the json module I could access the 
        # keys that are in the json

        print(content["name"])
        print(content)

except FileNotFoundError:
    print("File is not found")

except PermissionError:
    print("You don't have access to this file")

try:
    with open(file_path_csv, "r") as file:
        # content = file.read() -> both read the file
        content = csv.reader(file)

        # here is the same that works with the json module
        # it offers more ways to access data

        for line in content:
            print(line)

except FileNotFoundError:
    print("File is not found")

except PermissionError:
    print("You don't have access to this file")
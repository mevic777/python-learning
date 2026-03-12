# Python writing files (.txt, .json, .csv)

txt_data = "I like pizza !"

# file_path = "output.txt"
# file_path = "output.json"
file_path = "output.csv"

# with open(file_path, "w") as file: # returns a File Object
#     file.write(txt_data)
#     print(f"The information was written in {file_path}")

# try:
#     with open(file_path, "x") as file:
#         file.write(txt_data)
#         print(f"The information was written in {file_path}")
# except:
#     print("That file already exists")

# Append data
# try:
#     with open(file_path, "a") as file:
#         file.write("\n" + txt_data)
#         print(f"The information was written in {file_path}")
# except:
#     print("That file already exists")


# Collection example
# employees = ["Eugene", "Squidward", "Patrick", "Spongebob"]

# try:
#     with open(file_path, "a") as file:
#         for employee in employees:
#             file.write("\n" + employee)
#         print(f"The information was written in {file_path}")
# except:
#     print("That file already exists")

# Dictionary -> .json

# import json

# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }

# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4) # -> convert our dictionary in json
#         print(f"The information was written in {file_path}")
# except:
#     print("That file already exists")

import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 38, "Unemployeed"],
             ["Sandy", 27, "Scientist"]]

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)

        for row in employees:
            writer.writerow(row)

        print(f"The information was written in {file_path}")
except:
    print("That file already exists")
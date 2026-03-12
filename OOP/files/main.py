import os # library working with the system

file_path = "test.txt" # relative path

file_path_stuff = "stuff/test.txt" # relative path

file_stuff_desktop = "C:/Users/koval/Desktop" # absolute file path

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile():
        print(f"{file_path} is file")
    elif os.path.isdir():
        print(f"{file_path} is directory")
else:
    print("That location doesn't exist")




if os.path.exists(file_path_stuff):
    print(f"The location '{file_path_stuff}' exists")

    if os.path.isfile():
        print(f"{file_path_stuff} is file")
    elif os.path.isdir():
        print(f"{file_path_stuff} is directory")
else:
    print("That location doesn't exist")





if os.path.exists(file_stuff_desktop):
    print(f"The location '{file_stuff_desktop}' exists")

    if os.path.isfile():
        print(f"{file_stuff_desktop} is file")
    elif os.path.isdir():
        print(f"{file_stuff_desktop} is directory")
else:
    print("That location doesn't exist")
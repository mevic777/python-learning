name = input("Enter your full name: ")
phone_numer = input("Enter your phone number: ")

result = len(name) # length of the string
result1 = name.find(" ") # find the a character within string, the first occurence
result2 = name.rfind("s") # find the last occurence of a character within a string
# if no results, it returns -1

result3 = name.capitalize() # capitalize the string
result4 = name.upper() # make uppercase all the letters
result5 = name.lower() # make lowercase all the letters
result6 = name.isdigit() # if a string contains only digits, it will show True or False
result7 = name.isalpha() # if a string contains only alphabetical characters, if it contains space it will also show False

result8 = phone_numer.count("-") # it count how many occurences of a character is in a string
result9 = phone_numer.replace("-", " ") # it replace the first character, with the second argument of the function


print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
#print(help(str)) # offers all the string functions in the terminal


# username validation

username = input("Enter a username: ")
length = len(username)

if length > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username cannot contain numbers")
else: 
    print(f"Welcome, {username}")

credit_card = "1234-5678-9012-3456"

# string indexing 
# string[start : end : step]

print(credit_card[0])
print(credit_card[0:4]) # indexing of strings are exlusive
print(credit_card[5:9])
print(credit_card[-1]) # last index in the string

last_four_digits = credit_card[-4:]
print(f"XXXX-XXXX-XXXX-{last_four_digits}")

reverse_card = credit_card[::-1] # reverse of the string
print(reverse_card)
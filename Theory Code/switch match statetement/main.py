# def is_weekend(day):
#     match day:
#         case 1:
#             return "It is Monday"
#         case 2:
#             return "It is Tuesday"
#         case 3:
#             return "It is Wednesday"
#         case 4:
#             return "It is Thursday"
#         case 5:
#             return "It is Friday"
#         case 6:
#             return "It is Saturday"
#         case 7:
#             return "It is Sunday"
#         case _:
#             return "Not a valid day"
        

# def is_weekend(day):
#     match day:
#         case "Monday":
#             return "It is Monday"
#         case "Tuesday":
#             return "It is Tuesday"
#         case "Wednesday":
#             return "It is Wednesday"
#         case "Thursday":
#             return "It is Thursday"
#         case "Friday":
#             return "It is Friday"
#         case "Saturday":
#             return "It is Saturday"
#         case "Sunday":
#             return "It is Sunday"
#         case _:
#             return "Not a valid day"

# def is_weekend(day):
#     match day:
#         case "Monday":
#             return False
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thursday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return True
#         case "Sunday":
#             return True
#         case _:
#             return "Not a valid day"






# in match / switch statement the logic operator "or" and "and" ~ "|" and "&"







def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:
            return "Not a valid day"



print(is_weekend("Monday"))

numbers = [1, 2, 3, 4, 5]

if 1 in numbers:
    print(True)
        
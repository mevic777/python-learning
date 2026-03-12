word = "APPLE"

letter = input("Guess the letter in the secret word: ")

if letter in word:
    print(f"{letter} is in {word}")
else:
    print(f"{letter} is not in {word}")

if letter not in word:
    print(f"{letter} is not in {word}")
else:
    print(f"{letter} is in {word}")

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is our student")
else:
    print(f"{student} was not found")


grades = {
    "Sandy": "A",
    "Squidword": "B",
    "Spongebob": "C",
    "Patrick": "D"
}

student = input("Enter the name of a student: ")

if student in grades.keys():
    print(f"{student} is found")
else:
    print(f"{student} was not found")

email = "kovalimarius@gmail.com"

if "@" in email and "." in email:
    print("This is a valid email.")
else:
    print("This is not a valid email")

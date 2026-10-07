###Prompt the user to enter their age

age = int(input("Please enter your age: "))
if age < 5:
    price = 0
elif age < 12:
    price = 8
elif 13 < age < 64:
    price = 15
else:
    price = 10


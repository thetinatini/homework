# DEFINE VARIABLES
pin = 1234
tries = 0

# WHILE LOOP
while tries < 3:
    password = input("Please enter the password right now sir:")
    tries += 1

    # CHECK IF PASSWORD IS CORRECT
    if password == str(pin):
        print("Access granted")
        # END PROGRAM
        break
    # USER ENTERED INCORRECT PASSWORD
    else:
        if tries >= 3:
            print("Card blocked!")
        print("Incorrect PIN. Remaining attempts:", 3 - tries)


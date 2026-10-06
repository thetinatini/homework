# DEFINE VARIABLES
n = int(input ("please enter the number: "))
sum = 0


# START FOR LOOP - CODE RUNS FOR EACH NUMBER
for i in range (1 , n):

    # CHECK IF IT IS EVEN
    if i % 2 == 0:

        #print ("This is i: ", i)
        sum += i
        print ("This is sum: ", sum)


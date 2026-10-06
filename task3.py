#DEFINE VARIABLES

#ASK USER FOR INPUT
txt = input ("please enter the text: ")
#print("This is the input: ", txt)

# START FOR LOOP - CODE RUNS FOR EACH CHARACTER
for i in txt:
    #CHECK IF CHARACTER IS A DIGIT
    if i.isdigit():
        #REPLACE CHARACTER WITH NOTHING
        txt = txt.replace(i, "")

    else:
        continue

# PRINT OUTPUT
print("This is the output: ", txt)

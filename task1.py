### Create Empty List

scores = []

#Add Items to List 

scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)

#print List

print(scores)

#remove 45 from the list
scores.remove(45)

#print maximum,minimum, and avg
print("This is the highest score:", max(scores))
print("This is the lowest score:", min(scores))

# avg is total divided by lenghth of list
print("This is the average score:", sum(scores)/len(scores))

print("This is the length of the list:", len(scores))

#sort list
scores.sort()
print("These are the scores in ascending order:", scores)

#create new empty list
new_scores = [] 

#begin for loop
for score in scores:
    if score >= 60:
        new_scores.append(score)
    else: 
        continue

    #print passes scores
print("These are the passing scores:", new_scores)






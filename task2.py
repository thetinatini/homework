#Create inventory list
inventory = ["apple", "banana", "orange", "apple", "kiwi", "apple"]

#ceate new items list
new_items = ["mango", "grape"]

#print number of apples using .count()
print("there are" , inventory.count("apple"), "apples in the inventory rihght now.")

#print index (location) of orange using.index()
print("orange is in index number", inventory.index("orange"), "in the inventory right now.")

#add new list to end of inventory list using .extend()
inventory.extend(new_items)

print (inventory[::-1]) #print inventory in reverse order
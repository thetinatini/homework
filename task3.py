#Create list of locations
locations = [
    ("Tbilisi, 41.71, 44.82"),
    ("Batumi, 41.64, 41.63"),
    ("Kutaisi, 42.26, 42.71")
]

for location in locations:
    print("City:",location[0],", Latitude:",location[1],", Longitude:",location[2])

#create new list
city_names = []

for location in locations:
    city_names.append(location[0])
    
print("City names:", city_names)
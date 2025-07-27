# SETS Important note: Sets are unordered, unchangeable and unindexed. Also doesnt allow duplicates.

# Creating sets
setexample1 = {'apple', 'orange', 'banana', 'apple', 3}

print(setexample1)

# Add and Remove Items

setexample1.add('pinapple')
print(setexample1)

setexample1.discard('pinapple')
print(setexample1)

# Set Operations (union, intersection, difference)

# Union
setexample2 = {'apple', 3, 'microsoft'}
setexample3 = setexample1.union(setexample2)
print(setexample3)

#Intersection
setexample4 = setexample1.intersection(setexample2)
print(setexample4)

#Difference
setexample5 = setexample1.difference(setexample2)
print(setexample5)

setexample6 = setexample2.difference(setexample1)
print(setexample6)

# Loop Through Set

for x in setexample1:
    print(x)


# Dictionaries

# Create a Dictionary
newdict = {
    'name': 'Umit',
    'age': 37,
    'sex': "Male"
}
print(type(newdict))

# Access Values
print(newdict['age'])
print(newdict.get('age'))

# Update and Add Items
newdict['age'] = 38
print(newdict)

# Remove Items
newdict.update({'weight': 104})
print(newdict)

newdict.pop("weight")
# Or del(newdict['weight'])
print(newdict)


# Loop Through a Dictionary

for x in newdict:
    print(x, "for only keys")
    
for x in newdict:
    print(newdict[x],"for only values") 

for x in newdict.values(): 
    print(x, "looping using values() method for only values")

for x in newdict.keys():
    print(x, "looping using keys() method for only keys")

for x,y in newdict.items():
    print(x,y, "looping using items() method for only key value pairs")

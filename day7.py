# LISTS
# Crate a List

fruits = ['apple', 'banana', 'orange', 'pear', ['trousers', 't-shirt'], 5]

# Access Elements

first_element = fruits[0]
print(first_element)

last_element = fruits[-1]
print(last_element)

get_complex_element = fruits[-2][0]
print(get_complex_element)

# Modify the List

fruits.append('new item')
print(fruits)
fruits.insert(1, 'potato')
print(fruits)
fruits.remove(5)
print(fruits)
fruits[1:3] = ['balta']
print(fruits)

# Iterate through the List

for i in range(len(fruits)):
    if fruits[i] == 'balta':
        continue
    print(i)
    

#TUPLES

#Create a Tuple

first_tuple = ('car', 'bycicle', 'motorcycle')
print(first_tuple)
print(type(first_tuple))

# Access Elements

first_tuple_element = first_tuple[0]
print(first_tuple_element)

# Tuple Operations

second_tuple = ('truck', 'bus')
concat = first_tuple + second_tuple
print(concat)

repetition_tuples = second_tuple * 3 
print(repetition_tuples)

if('car' in first_tuple):
    print('We got a car in this mofo!')

my_list = list(second_tuple)
my_list.append('romorkor')
tuple(my_list)
print(type(my_list))
print(my_list)
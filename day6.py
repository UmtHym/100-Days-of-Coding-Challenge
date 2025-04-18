# Simple Function
def greet_user(name):
    print(f"Hello, {name}")
# greet_user("Umit")

# Default and keyword arguments
def greet_user(name = "Guest"):
    print(f"Hello, {name}")
# greet_user()

# Function With Return Values
def rectangle_area(length, breadth): 
    return float(length) * float(breadth)
# print(rectangle_area(2,4))

# Variable Scopes

# 1. Define a Global vartiable and print its value
name = "Umit"

# 2. Write a function and assign a new value to the same varible inside the function and then print it.
def rename(n):
    name = n
    return name
# print(rename("Alex"))

# 3. Print the variable again outside the function again to observe that its value didn't change.
# print(name)

# 4. Write another function that access the global variable using the global keyword and then update its value.
def chage_global_var():
    global name
    name = "Alex Desouza"

chage_global_var()

 # 5. Print the variable again outside the function. Verify that it's value now got updated.
print(name)


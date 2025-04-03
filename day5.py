### if-Else Statements ###
# Program 1: Check if number is even/odd
number = int(input("Write an number to check if its even or odd: "))
if(number % 2 == 0):
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# Program 2: Determine age category
number = int(input("\nEnter an age to determine seniority:"))
if(number <= 18):
    print("You are a child!")
if(18 < number < 30):
    print("You are a teenager!")
if(30 < number < 60):
    print("You are a adult!")
else:
    print("You are a senior!")

    
### Nested If-else Statements ###
# Program 3: Using nested if -else, dind the largest of the three numbers
num1 = int(input("\nEnter the first number:"))
num2 = int(input("\nEnter the second number:"))
num3 = int(input("\nEnter the third number:"))

if(num1 >= num2):
    if(num1 >= num2):
        print(f"The largest number is {num1}.")
    else:
        print(f"The largest number is {num3}.")
else:
    if(num2>= num3):
        print(f"The largest number is {num2}.")
    else:
        print(f"The largest number is {num3}.")

### For Loop ###
# Program 4: Calculate the sum of all numbers up to the given input number(Gausses formula)

number = int(input("\nEnter a positive number to calculate the sum up to that number:"))
sum = 0
for n in range(1, number + 1):
    sum += n
print(f"the sum of all numbers from 1 to {number} is {sum}")

### While loop ###
# Program 5: Calculate the factorial of a given number
number = int(input("\nEnter a number to calculate its factorial: "))
factorial = 1
while n > 1:
    factorial *= number
    number -= 1

print(f"The factorial of the {number} is {factorial}.")

print("\nCongratulations on completing Day 5 of the 100 Days of Ptyhon code challenge!\n")

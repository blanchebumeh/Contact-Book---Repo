print("Hello World")
name = "Blanch is"
age = 19
#state = "name + is ", age
print(name, age)
print("I like python")

#Variables = A container for a value (string, interger, float, boolean)
#example
first_name = "Blanche"
age = 19
print(first_name)
print(f"my name is {first_name}")
print(f"I am,{age}")

#sting is a sequence of text or characters
#integers
age= 10
print(f'age is {10} and {first_name} is 19')
#float
price = 70.0
gpa = 3.4
print(f"the price is {price}")
print(f"my gpa is {gpa}")
#Bolean(True or False)
is_student = True
print(f'Are you a student?: {is_student}')
if is_student:
    print("You are a student")
else:
    print("You are not a student")
for_sale = False
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")
is_online = True
if is_online:
    print("Is online")
else:
    print("Is not online")

#Typecasting = the process of converting = variable from one data type to another, str(), int(),float(),bool()
name = "Blanch"
age = 10
gpa = 20.2
is_student = True
type(name)
print(type(gpa))
gpa = int(gpa)
print(gpa)
age =float(age)
print(age)
name = bool(name)
print(name)

#Input = A function that prompts the user to enter data
#Returns the entered data as a string
#how to accept an input in python

# age = input("what is your age?:")
# print(f'Hello, {age}')
# name = input("what is your name?")
# print(f"Greetings {name}!")
# gpa = input("what is your gpa? ")
# print(f"my gpa is {gpa}")

# new_name = input("What is your new name?:")
# new_age = input("How old are you?: ")
# new_age = int(new_age)
# new_age = new_age + 2
# print('Happy Birthday')
# print(f"You are {new_age} years old")

#Exercise 1 calculate the area of a rectangle
# l = int(input("Enter the length of rectangle"))
# w = int(input("Enter 4the width of rectangle"))
# A = l*w
# print(f"The area is: {A}cm^2")

# age_student = int(input("Enter your age"))

# if age_student >= 18:
#     print("he/she is old enough to vote")
# else:
#     print("he/she is not old enough to vote")



# Ques1 = input("How your feeling today")
# Ques2 = input("Why your having that feeling")

# print(Ques1)
# print(Ques2)

name = input("Enter your name")
age = int(input("Enter your age"))
if age >= 18:
    print("born in the 2000s")
else:
    print("not born in the 2000s")

currentYear = 2024
DOB = currentYear-age
print(DOB)


#Write a python code where you can save a contact

user_name = input("enter your names: ")
user_contact = int(input("enter your contact infor: "))
print(user_contact)
if user_contact == 9:
    print(f"{user_contact} Accepted")
elif user_contact >= 9:
    print(f"Your {user_contact} number if valid")
elif user_contact <= 9:
    print(f"Your {user_contact} number if invalid")


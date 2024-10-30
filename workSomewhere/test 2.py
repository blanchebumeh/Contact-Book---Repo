# #Exercise 1 calculate the area of a rectangle
# l = int(input("Enter the length of rectangle"))
# w = int(input("Enter 4the width of rectangle"))
# A = l*w
# print(f"The area is: {A}cm^2")

# #Exercise 2 shopping cart program
# item = input("what item would you like to buy?")
# price = float(input("what is the price?"))
# quatity = int(input("How many would you like?:")) 
# total = price*quatity
# print(total) 
# print(f"You have bough {quatity} x {item}/s")
# print(F"Your total is {total}CFA") 

# #Exercise 3 = creating a madlibs game
# #word game where you create a story
# #by filling in blanks with random words

# adjective1 = input("Enter an adjective")
# noun1 = input("Enter a nound")
# adjective2 = input("Enter an adjective")
# verb1 = input("Enter a verb")
# adjective3 = input("Enter an adjective")

# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

#Practice

# Day = input("Enter the day of today")
# Place = input("Enter your place of work")
# Hour = input("Enter the number of hours worked ")
# Meetings = input("How many meetings did you attend?")
# Objective = input("Enter yes or no if you completed your task today")


# print(f"Today is {Day}")
# print(f"I am going to my job side at {Place}.")
# print(f"I have been able to work for {Hour}hours today")
# print(f"I attended {Meetings} meetings")
# print(f"I also completed the objective for the day? {Objective}")

#Arithmetic operators and build in math functions
#basic Arithmetic operators
#to incremment a value by 1 or to add a value by 1 use the %= 1, += 1, -= 1,.... example
#modulos gives us he remainder of any division
#augmented assignment operators( %= 1, += 1, -= 1,)
colleagues = 2
colleagues -= 2
print(colleagues)

# #Build in math functions
# x = 30.2
# y = 4
# z = 6
# #The round function
# result = round(x)
# print(result)
# #the absolute value is the distance away from zero as a whole number
# results = print(abs(y))
# #pow - base and exponent
# result = print(pow(4,30))
# results = print(max(x,y,z))
# #pie radius square and exponential values
# import math
# print(math.pi)
# print(math.e)
# p = 10.2
# print(math.sqrt(p))
# #ceil function always rounds a floating point up
# print(math.ceil(p))
# #floor function always rounds a floating point down
# print(math.floor(p))

# #Exercises calculate the circumfrence of a cicle
# import math
# r = float(input("enter the radius of a circle"))
# c = 2 * math.pi * r
# print(round(c)) 
# #The area of a circle
# import math 
# r = int(input("Enter the radius of a circle"))
# a = math.pi * r**2
# print(a)

#Exercise finding the hypertenus of a triangle
# import math
# a = float(input("enter the side a"))
# b = float(input("enter the side b"))
# c = math.sqrt(pow(a,2) +pow(b,2))
# print(round(c))

#if = use to do come code only if some condition is true , else do something else
# age = int(input("Enter your age"))

# if age >= 18:
#     print("You are now signed up ")
# elif age < 0:
#     print("You have not been born yet")
# elif age >= 100:
#     print("You are now signed up")
# else:
#     print("You must be 18+ to sign up ")

#Example 2 for if statements
# response = input("Would you like food? Y/N")
# if response == "Y":
#     print("have some food!")
# else:
#     print("no food for you!")

#Example 3
# Voting_age = int(input("Enter your age"))
# if Voting_age != 18:
#     print("You must be 18+ to vote")
# else:
#     print("You are of age to vote")

#Example 4
# for_sale = False
# if for_sale:
#     print("This item is for sale")
# else:
#     print("This item is not for sale")

#EXercise python calculator

# operator = input("Enter an operator(+ - * /, %): ")
# num1 = float(input("enter the first number: "))
# num2 = float(input("enter the second number: ")) 
# if operator == "+":
#     result = num1 + num2
#     print(result)
# elif operator == "-":
#     result = num1 - num2
#     print(result)
# elif operator == "*":
#     result = num1 * num2
#     print(result)
# elif operator == "/":
#     result = num1/num2
#     print(result)
# elif operator == "%":
#     result = num1 % num2
#     print(result)

#Exercise 5: python weight converter

# weight = float(input("enter your weight"))
# unit = input("Enter kilograms or pounds? (K or L)")
# if unit == "K":
#     weight = weight*2.205
#     unit = "Lbs"
# elif unit == "L":
#     weight = weight/2.205
#     unit = "Kgs"
# else:
#     print(f'{unit} was not valid')
# print(f"Your weight is: {round(weight, 2)} {unit}")

#Exercise 6
# unit = input("is this temp in celsuis or fahrenheit(C/F): ")
# temp = float(input("enter your temp: "))

# if unit == "C":
#     temp =round((9*temp)/ 5 +32, 1)
#     print(f"the temp in farenheit is: {temp}F")
# elif unit == "F":
#     temp = round((temp - 32) *5/9, 1)
#     print(f"the temp in celsuis is: {temp}C")
# else:
#     print(f"{unit} is an invalid unit of measurement")



#Logical operators = evaluate multiple conditions(or, and, not)
                     # or = at least one condition must be True
                     # and = both conditions must be True
                     # not = inverts the condition(not false, not true)
# or condition
# temp = float(input("enter the temp of day: "))
# is_raining = False
# if temp > 35 or temp < is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# #and condition
# temp = 30
# is_sunny = True
# if temp >= 28 and is_sunny:
#     print("It is hot outside")
#     print("it is sunny")
# elif temp <= 0 and is_sunny:
#     print("It is cold outside")
#     print("it is sunny")


#Conditional expressions = A one-line shortcut for the if-else statement(ternary operator)
                           #print or assign one of the two values based on a condition 
                           # Return X if condition is true else return Y
# num = 6
# #print("positive" if num > 0 else "negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

#STRING METHODS = a string is a series of characters
# name = input("enter your full name: ")
# result = len(name)
#to find the first occurence of a string , use the name.find function
# result = name.find(" ")
#to find the last occurence of a string , use the name.rfind function
#result = name.rfind("o")
# We can capitalise the first letter of a string by using the capitalise function(name.capitalize)
# result = name.capitalize()
# We can upper case function to capitalise all letters of a string by using the upper function(name.upper)
# result = name.upper()
# We can use the lower case function to lower all letters of a string by using the lower case function(name.lower)
# result = name.lower()


a, b = map(int, input().split())
print(a // b)


# print(result)
# Exercise write a python code that takes the employees name, define time range,and check when am employee enters their time if they came early or not

name_employee = input("Enter your name: ")
Time_in = int(input("Enter your time in: "))
On_time = 9.10
Late = 9.20
if Time_in <= On_time:
    print(f"You are On_time, {name_employee}")
elif Time_in > Late: 
    print(f"You are Late, {name_employee}")
elif Time_in == 0:
    print("Absent from work")





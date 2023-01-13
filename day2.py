# Data Types, Numbers, Operators, Type conversion,f-strings

# Data Types

# Strings:

#print("Hello")

# print("Hello"[0])
# print("Hello"[4])
# print ("123" + "123")  #quotes make it a string

# Integer: Whole numbers without decimal points.

#123 = Integer

# print(123 + 456)

# print(676_676_896+ 666_444)

# Float: Numbers with decimals

# 3.88888

#Boolean: 

# True
# False

#Quiz
# street_name = "Abbey Road"
# print(street_name [4] + street_name [7])

# num_char =len(input("What is your name? ") )
# new_num_char = str(num_char)
# print("Your name contains " + new_num_char + " Characters")


# print(70 + float("100.5"))

# Coding exercise:
#Write  a programme that adds the digits numbers. e.g if the input was 35, then the output should be 3+5=8
# two_digit_number =input("Type a two digit number ")
# #Check the data type of the two_digit_number
# print(type(two_digit_number))
# #Get the first and second digits using subscripting then convert string to int.
# first_digit_number = two_digit_number[0]
# second_digit_number = two_digit_number[1]
# #Add the two digits together
# result = int(first_digit_number) + int(second_digit_number) 
# print(result)
#addition
# 1+1
# #multiplication
# 2*2
# #raise to the power
# 2**3
# #division
# 2/3
#Order of priority:
#PEMDAS(LR)
#calculations go from Left to Right
# Parenthesis()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -
# print(3+3*3/3-3)

#BMI calculator exercise:
# height =input("enter you height in m: ")
# weight = input("Enter your weight in kg: ")
# bmi = int(weight)/ float(height)**2
# bmi_as_int = int(bmi)
# print(bmi_as_int)

# #print 7 divided by 6
# print(7/6)
# #round up to a whole number
# print(round(7/6))
# #rounds up to whole number and specified number after decimal 
# print(round(7/6, 2))
# print(round(6.888888 ,2))

# score = 0
# height = 1.8
# is_winning = True
# #fstring
# print(f"Your score is {score}, your height is {height}, you are winning is {is_winning})")

#Life in week Exercise:
#Create a programme using maths and f-string that tells us how many days,weeks, months we have left if we live until 90 years.

# age=input("What is your current age ")
# age_as_int = int(age)
# years_remaining= 90 - age_as_int
# months_remaining = years_remaining * 12
# weeks_remaining = years_remaining * 52
# message = (f"You have {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks remaining.")
# print(message)

# Day 2 Project: Tip Calculator
print("Welcome to tip calculator!")
bill=float(input("What was your total bill? $"))
tip=int(input("how much tip would you like to give? 10,12, or 15? "))
people=int(input("How many people to split the bill?" ))
bill_with_tip= tip/100*bill+bill
print(bill_with_tip)












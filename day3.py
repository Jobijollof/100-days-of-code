#Conditional Statements. Logical operators, Code Blocks and scope.

# print("Welcome to the Rollercoaster!")
# height= int(input("What is your height in cm? "))
# if height > 120:
#     print("You get a ticket")
# else: 
#     print("You need to grow taller")
    
# #Greater than or equal to   

# print("Welcome to the Rollercoaster!")
# height= int(input("What is your height in cm? "))
# if height >= 120:
#     print("You get a ticket")
# else: 
#     print("You need to grow taller") 
    
#Comparison operators
# > Greater than
# < Less than
# >= Greater than or equal to 
# <= Less than or equal to
# == equal to
# != Not equal to
# = One equal sign is giving a value to a variable.

# Odd or Even exercise:
# number= int(input (" Which number do you want to check ? "))
# if number % 2 == 0:
#     print("This is a even number.")
# else:
#     print("This is an odd number")
 
#If/Else Elif Statement.

# print("Welcome to the Rollercoaster!")
# height= int(input("What is your height in cm? "))
# if height >= 120:
#     print("You get a ticket")
#     age = int(input("input your age "))
#     if age >= 18:
#         print("You are paying the full adult price")
#     elif age <18 == 12:
#         print("You are paying 7$")
#     elif age <= 12:
#         print("You are paying 2$")
# else:
#     print("You need to grow taller")
    
    
    
#BMI 2.0 Exercise:
height = float(input("Enter your height in m: "))
weight = float (input("Enter your weight in kg: "))
bmi = round(weight / height **2)
if bmi < 18.5:
    print(f" Your bmi is {bmi}, You are underweight")
elif bmi < 25:
    print(f" Your bmi is {bmi}, You have a  normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, You are over weight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, You are Obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese") 




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

print("Welcome to the Rollercoaster!")
height= int(input("What is your height in cm? "))
if height >= 120:
    print("You get a ticket")
    age = int(input("input your age "))
    if age >= 18:
        print("You are paying the full adult price")
    elif age <18 == 12:
        print("You are paying 7$")
    elif age <= 12:
        print("You are paying 2$")
else:
    print("You need to grow taller")
    



#else: 
    #print("You need to grow taller")
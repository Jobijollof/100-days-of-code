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
# height = float(input("Enter your height in m: "))
# weight = float (input("Enter your weight in kg: "))
# bmi = round(weight / height **2)
# if bmi < 18.5:
#     print(f" Your bmi is {bmi}, You are underweight")
# elif bmi < 25:
#     print(f" Your bmi is {bmi}, You have a  normal weight.")
# elif bmi < 30:
#     print(f"Your bmi is {bmi}, You are over weight")
# elif bmi < 35:
#     print(f"Your bmi is {bmi}, You are Obese")
# else:
#     print(f"Your bmi is {bmi}, you are clinically obese") 

#Leap Year exercise:
# year= int(input("What year do you wish to check? "))
# if year % 4 == 0:
#     print("Leap year")
# elif year % 100 == 0:
#     print("Leap year")
# elif year % 400 == 0:
#     print("Leap year")
# else:
#     print("Not Leap year")


# print("Welcome to the Rollercoaster!")
# height= int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#      print("You get a ticket")
#      age = int(input("input your age "))
#      if age >= 18:
#          bill = 12
#          print("Adult ticket $12")
#      elif age <18 == 12:
#          bill = 7
#          print("Youth ticket $7")
#      elif age <= 12:
#          bill = 2
#          print("Child ticket $2")
#      wants_photo = input("Do you want a photo taken? Y or N.")
#      if wants_photo == "Y":
#         bill = bill + 3
#         print(f"Your final bill is ${bill}")
# else:
#     print("You need to grow taller")
    
# # Pizza Order Exercise:
# print("welcome to python pizza deliveries") 
# size= input(" What size of pizza do you want S, M, or L ")
# add_peperoni=input("Do you want peperoni? Y or N ")
# extra_cheese= input("Do you want extra cheese? Y or N ")
# bill = 0
# if size == "S":
#     bill = 15
#     print(f"Your bill is ${bill} ")
# elif size == "M":
#     bill = 20
#     print(f"Your bill is ${bill}")
# elif size == "L":
#     bill=25
#     print(f"Your bill is ${bill}")
# if add_peperoni == "Y":
#     if size == "S":
#      bill = bill + 2
#     else:
#      bill = bill + 3
#     print(f"Your final bill is ${bill}")
# elif extra_cheese == "Y": 
#     bill = bill + 3
#     print(f"Your final bill is {bill}")
# else:
#     print("Thank you for stopping by")

# Logical operators (Combining  multiple conditions):
#And (both conditions have to be true or else it amounts to false)
# Or (if just one condition is true or are both true. This evaluates to false when both statements are false)
# Not(reverses a condition )

#print("Welcome to the Rollercoaster!")
# height= int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You get a ticket")
#     age = int(input("input your age "))
#     if age < 12:
#         bill = 5
#         print("child tickets are $5")
#         if age <= 18:
#             print("Youth tickets are $7.")
#     elif age >=45 and age <=55:
#         print("Everything is going to be ok have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12")
#         wants_photo = input("Do you want a photo taken? Y or N.")
#         if wants_photo == "Y":
#             bill = bill + 3
#             print(f"Your final bill is ${bill}")

#Love Calculator exercise:
# print("Welcome to the love calculator")
# name1 = input("What is your name \n")
# name2 = input("What is your name? \n")
# combined_string = name1 + name2
# lower_case_string = combined_string .lower()
# t=lower_case_string.count("t")
# r=lower_case_string.count("r")
# u=lower_case_string.count("u")
# e=lower_case_string.count("e")
# true = t+r+u+e
# l=lower_case_string.count("l")
# o=lower_case_string.count("o")
# v=lower_case_string.count("v")
# e=lower_case_string.count("e")
# love = l+o+v+e
# love_score = int(str(true) +str(love))
# print(love_score)
# if (love_score < 10) or (love_score > 90):
#     print(f"Your love score is {love_score}, you go together")
# elif(love_score>=40) and (love_score<=50):
#     print(f"Your score is {love_score} happy life.") 
# else:
#     print(f"Your score is {love_score}") 
    
#Project Day 4:
print("Welcome to treasure Island ")
print("Your mission is to find the treasure ")
#to escape the apostrophe we use backlash like below
option1 = input('You\'re at a crossroad,"Where would you like to go? Type "Left" or "Right"? ' ).lower() 
if option1 == "left":
    option2= input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across ').lower()
    if option2 == "wait":
        option3 = input(' You arrived in the island unharmed.There is a house with three doors. One "red", one "yellow", one "blue". Which color do you choose?').lower()
        if option3 == "yellow":
         print("You don win!!!")
        elif option3 == "blue":
         print("issolova for you")
        elif option3 == "red":
         print("goodbye and God bless")
        else:
            print("If God be for us")
    
    else:
        print("You have been attacked by a shark")
else: 
  print(" You fell into a ditch, Game Over.")
      

         
         
         
    
    

          
          
        
    

    


 
    
 




   
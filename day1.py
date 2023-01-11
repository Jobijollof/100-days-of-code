# Strings
# Exercise 1: Print Function
print("Day 1 - Python print function")
print("The function is declared like this:")
print("print('what to print')")

# use back slash and n (\n) to use a single print statement to print multiple lines.

print("Hello world!\nHello world!\nHello world!")

# Concatenate strings using the plus sign. To add a space, leave a space after hello or before Jobina or " "

print("hello" + "Jobina")
print ("Hello " + "Jobina")
print ("Hello" + " Jobina")
print ("Hello"+ " "+ "Jobina")

#Indentation is very important in python.(indentation error)
#Syntax is important(Syntax error)

#Exercise 2: Input function. input() will get user to input in console
#Then print () will print hello and the user input

input("what is your name?" )
print("Hello" + " " + input("What is your name? " ))

# Exercise 3: Len function.  (The len function prints out the total number of words the user has imputed)

print(len(input("What is your name? ")))

#Variables:

name= input("What is your name? ")
print(name)
name= "Jack"
print(name)

name= "Jobina"
print(name)

name = input("what is your name? ")
length = len(name)
print(length)

#To switch variables
#a = (5)
#b = (6) 
#answer
#c = a
#a = b
#b = c

#Project: Band name generator
#Create greeting for your programme
# Ask user for city they were born
# Ask user for pet name
#Combine nme of city and pet name to come up with band name
# Make sure input cursor starts on the next line.(\n)

greeting = ("Good afternoon and welcome to band name generator")
print(greeting) 
user_city = input("what city where you born?\n ")
user_pet = input("what is the name of your pet?\n ")
print("The name of your band could be" +  user_city  " " + user_pet)

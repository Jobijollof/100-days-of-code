#Random number:
#To get random numbers we have to import the random module. Ask python will tell you how to use all the modules
#To use a module, you have to import it first.
#random module was created by the python team to help generate random numbers without getting into all the complexities required



#Random integer: This will give you random integers including the numbers stated in the range.
 
import random
random_integer = random.randint(1,10)
print(random_integer)

#To create my own module: Write and save my_module.py. Import my_module,use module.

import my_module
print(my_module.pi)

#Random Float numbers: #random.random(): This returns the next random floating point number between {0 to 0.1}
#note that 1 will not be printed. It will print till 0.9999999

random_float = random.random()
print(random_float)

#random float numbers between (0 to 5)
float_number = random.uniform(1,5)
print(float_number)

#Love score generator:
love_score = random.randint(1,100)
print(f" Your love score is {love_score}")

#Exercise:Heads or tail
print('Welcome to the "Heads" or "Tail" challenge')
random_numbers = random.randint(1,10)
if random_numbers == 5:
  print("Heads")
else:
    print("tails")

#Python Lists: 
#Data Structure: A way of organising data in python.

fruits = ["oranges", "Mangoes", "Paw paw"]
print(fruits)
print(fruits[0]) #positive index
print(fruits[-1]) #negative index

names= ["Jobina", "Zite", "Tibe"] 
names[2]= "Tobe" #change a name on the list
print(names)

names= ["Jobina", "Zite", "Tibe"] 
names[2]= "Tobe" #change a name on the list
print(names)


names = ["Jobina", "Zite", "Tibe"] 
names.append ("Nkpami")   #add a  single name to the list using the append function
print(names)


names = ["Jobina", "Zite", "Tibe"] 
names.extend (["Nkpami", "Mummy ", "Daddy" ] )   #add a multiple names to the list using the extend function
print(names)


#1. String to List of Strings
# When we need to convert a string to a list in Python containing the constituent strings of the parent string (previously separated by some separator like ‘,’ or space), we use this method to accomplish the task.

# For example, say we have a string “Python is great”, and we want a list that would contain only the given names previously separated by spaces, we can get the required list just by splitting the string into parts based on the position of space.

# Let us look at an example to understand it better.

#given string
string1="Python is great"
 
#printing the string
print(string1) 
   
#gives us the type of string1
print(type(string1))  
 
print(string1.split()) #using the split function
#prints the list given by split()

# We consider a string, string1="Python is great" and try to convert the same list of the constituent strings
# type() gives us the type of object passed to the method, which in our case was a string
# split() is used to split a string into a list based on the given separator. In our code, the words were separated by spaces. By default, if we do not pass anything to the split() method it splits up the string based on the position of spaces
# Hence though we have not mentioned the separator parameter, the split() method gives us a list of the respective strings





# 2. String to List of Characters
# What if we need a list of characters present in a string? In that case, direct type conversion from string to list in Python using the list() method does the job for us.
# Certainly, if the input string is something like “abcd”, typecasting the string into a list using the list() method gives us a list having the individual characters ‘a’, ‘b’, ‘c’, ‘d’ as its elements. Take a look at the given example code below.


#given string
string1="AskPython"
 
#printing the string
print(string1)
#confirming the type()
print(type(string1))
 
#type-casting the string into list using list()
print("String converted to list :\n",list(string1))


# Understanding the code:
# Firstly here, we initialize a string, string1 as “AskPython” and print its type using the type() method
# And as we can observe, typecasting the string using the list() method gives us a list of the member characters, as required


# 3. List of Strings to List of Lists
# Here, we are going to see how we can combine both the above methods to convert a string to a list of character lists.
# Look at the below-given example carefully,

#
# Given string
string1="This is Python"
 
print(string1)
 
#converting string1 into a list of strings
string1=string1.split()
 
#applying list method to the individual elements of the list string1
list1=list(map(list,string1))
 
#printing the resultant list of lists
print("Converted to list of character list :\n",list1)

# Understand the code:

# In this case, after the initialization of the string string1, we use the first method and convert it into a list of strings
# That is, at this point string1 is a list of strings given by [ 'This', 'is', 'Python' ]
# Then we apply the list() method to all the elements of the list
# string1. As we saw in our previous case this gives us a list consisting of character lists. Note, mass type-casting was performed using the map() function


# 4. CSV to List
# A CSV( Comma Separated Values) string, as its name suggests is a string consisting of values or data separated by commas.
# Let us look at how we can convert the such type of string to a list in Python.

#given string
string1="abc,def,ghi"
print("Actual CSV String: ",string1)
print("Type of string: ",type(string1))
 
#spliting string1 into list with ',' as the parameter
print("CSV converted to list :",string1.split(','))


# Understand the code :
# Similarly, we initiate by considering a string string1 with various data or values separated by commas(‘,’)
# After printing it and its type(), we proceed by splitting it based on the parameter ‘,’
# This makes the values ‘abc’, ‘def’, and ‘ghi’ the elements of a list. In this way, we were able to extract values from a given CSV


# 5.A string consisting of Integers to a List of integers
# Now we are going to convert a string consisting of only integers separated by some space, comma, etc., to a list with integer elements.
# For example, look at the code below,

#string with integers seperated by spaces
string1="1 2 3 4 5 6 7 8"
print("Actual String containing integers: ",string1)
print("Type of string: ",type(string1))
 
#converting the string into list of strings
list1=list(string1.split())
print("Converted string to list : ",list1)
 
#typecasting the individual elements of the string list into integer using the map() method
list2=list(map(int,list1))
print("List of integers : ",list2)

# Now:

# We took a string, string1 as “1 2 3 4 5 6 7 8” and print it and its type() consecutively
# Then we split it using the split() method and store the resultant list into a list, list1. At this point, list1 holds [ ‘1’, ‘2’ , ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’ ] as we can see from the output, as expected
# Now we map the function int() throughout the list, typecasting each one of the elements into integers. And further, we store the typecasted mapped list into list2 and print the same
# As a result, we get a list consisting of the integer elements on which now we can perform arithmetic operations.

# Conclusion
# That’s all now, this was about converting strings into different lists using various methods. Try to use the one which suits your code and solves your purpose as well as meets up to your requirements. Questions in the comments are appreciated.

#Code Exercise:

 


 


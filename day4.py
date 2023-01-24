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
names.extend (["Nkpami", "Mummy ", "Daddy" ] )   #add a  single name to the list using the append function
print(names)

 


 


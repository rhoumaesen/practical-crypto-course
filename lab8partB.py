from random import *

# Generate a pseudo-random number between 0 and 1.
print(random())

#Generate a random number between 1 and 100
#To generate a whole number (integer) between one and one hundred use:
print(randint(1, 100)) # Pick a random number between 1 and 100.
#This will print a random integer. If you want to store it in a variable you can use:
x = randint(1, 100) # Pick a random number between 1 and 100.
print(x)
#Random number between 1 and 10
#To generate a random floating point number between 1 and 10 you can use the uniform() function
print(uniform(1, 10))
#Picking a random item from a list
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(items)
print(items)

#To pick a random number from a list:
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = sample(items, 1) # Pick a random item from the list
print (x[0])
y = sample(items, 4) # Pick 4 random items from the list
print (y)
#We can do the same thing with a list of strings:
items = ['Alissa','Alice','Marco','Melissa','Sandra','Steve']
x = sample(items, 1) # Pick a random item from the list
print (x[0])
y = sample(items, 4) # Pick 4 random items from the list
print (y)
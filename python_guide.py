"""
THINGS TO ADD

walrus operator (https://www.geeksforgeeks.org/python/walrus-operator-in-python-3-8/)
match cases (https://www.geeksforgeeks.org/python/python-match-case-statement/)
custom exceptions (https://www.geeksforgeeks.org/python/define-custom-exceptions-in-python/)
logging (https://www.geeksforgeeks.org/python/logging-in-python/)


extend() for arrays


add the various options sort() has for parameters

.update() can append multiple key/value pairs to a dictionary

generators and yield

itertools

"""



#------------------------------------- Assignment statements ----------------------------------------------

# this assigns 5 to x_assign and 6 to y_assign
x_assign, y_assign = 5, 6

# this will assing "red" to color, "4 door" to vehicle and "large" to size
arr_assign = ["red", "4 door", "large"]
color, vehicle, size = arr_assign

#------------------------------------ Ternary operator ----------------------------------------------------

"""
An assignment statement that encompasses if else statement in to one line. There are no 
elif, just a chain of else statements like below. The first else statement of 'else 15 if ter > 1' 
is operating similar to an elif. 
"""
ter = 5
ternary = 20 if ter > 6 else 15 if ter > 1 else 0 

# -------------- ------------------ Strings ---------------------------------------------------------------

# letter to ASCII
a = "a"
a_ascii = ord(a)

# ASCII (integer) to letter
int_to_letter = chr(100)  # this will assign the letter 'd' to the variable y

my_string1 = "Something"
find_character = my_string1.find("e")  # finds the index of the first occurence of "e"
my_string = my_string1.replace("i","a") # replaces "i" with "a"
my_str_count = my_string1.count("e")  # this will count the number of "e" in the string

my_string2 = "some"
my_string3 = "thing"
my_string4 = my_string2 + my_string3  # this will join the two strings

my_string5 = my_string4[:4]  # this will print the string form index 0 to index 3

my_str_arr = ["h","e","l","l","o"]
my_str_arr2 = "".join(my_str_arr)  # this will turn the aray into the string "hello"

my_string6 = my_string1.split() # this will turn a string into a list

"""
come back to this video and add some more of functions it references

https://youtu.be/PNSIWjWAA7o?t=963
"""


# ------------------------------------ Loops --------------------------------------------------------------

"""
This will start on 2, end on 19 and only print every 3rd element
"""
for i in range(2,20, 3):
  print(i)

# this will backwards iterate from 10 to 0
for j in range(10, -1, -1):
	print(j)

# this will loop through loop_arr and print the index and value of each element
loop_arr = ["a", "b", "c"]
for index, letter in enumerate(loop_arr):
	print(f"{index}:{letter}")

# use of continue and break
x = 5 
while True:
  x += 1 
  if x < 10:
    # this will stop the current iteration of the loop and not execute the code below it
    continue  
  print(x)
  if x > 20:
    # this will stop the loop entirely
    break

# for else
for i in [1,2,3,4,5]:
  if i == 3:
    print("3 was found")
    break
else:
  print("only executes if the if statement is never reached")

# zip is for iterating through multiple lists at the same time, similar to enumerate
names = ["Joe", "Hollie"]
ages = [49, 48]

for name,age in zip(names, ages):
  print(f"{name} is {age} years old")

 
#------------------------------------------ Array ----------------------------------------------------------

# array
# can also be aused as a stack by using only append() and pop()
arr = [3,2,1]
arr = arr + [5,6,7] # this will apend the list to arr
del arr[0]  # mno assignment is neede, this will delete the first element from the array
arr_copy = arr[:]  # creates a copy of the array, this is a separate object
arr2 = arr.copy()  # creates a separate copy of the array 
arr.append(5)
arr.pop(0)  # removes last element, this is how you use an array like a stack
arr.remove(2)  # deletes the object at index 2
arr.sort()   # sorts the array
arr.sort(reverse = True) # sorts then reverses the array
find_element = arr.index(5)   # returns the index where the first occurence of 5 is 

# list comprehension, this creates a new list of [10,12,14]
list_comp = [i*2 for i in [5,6,7]] 

# list comprehension with conditionals
list_comp2 = [True if i % 2 == 0 else False for i in arr]

#----------------------------------------- Set ---------------------------------------------------------------
my_set = set([1,2,3])
my_set2 = {19,20,21}
my_set.add(4) # adds 4 to the set
my_set.remove(1)  # removes 1 from the set, will throw an error is the number isn't present
my_set.discard(19) # removes 19 from the set and does not throw an error if it is not present
my_set.update([7,8,9]) # can add multiple elements to a set at the same time
my_set3 = my_set.union(my_set2) # this will combine two sets

my_set4 = {1,2,3,4,5}
my_set5 = {4,5,6,7,8}
# creates a new set comprised of the intersection between two sets
my_set6 = my_set4.intersection(my_set5) # this is {4,5}
# only the elements in my_set4 that it does not share with my_set5
my_set7 = my_set4.difference(my_set5) # {1,2,3}
# will combine the two sets except for their common elements
my_set8 = my_set4.symmetric_difference(my_set5) # {1,2,3,6,7,8}


#----------------------------------------- Tuple (they are immutable) ---------------------------------------
my_tup = (4,5)


#----------------------------------------- Deque ------------------------------------------------------------

# deque (you can also just use this as a queue)
from collections import deque
my_deque = deque[(7,8,9)]
my_deque.append(10)  # adds 10 to the end 
my_deque.appendleft(6)  # adds 6 to the beginning 
my_deque.pop()  # removes the last element 
my_deque.popleft()  # removes the first element
my_deque.count(7)  # counts the number of 7
my_deque.reverse()  # reverses the deque
my_deque.clear()  # clears the entire deque

#----------------------------------------- Dictionary --------------------------------------------------------

dictionary = {1:7, 2:5}
dictionary[5] = 19

# prints all of the keys in a dictionary
for key in dictionary.keys():
  print(key)

# prints all of the values in a dictionary
for value in dictionary.values():
  print(value)

# prints both key and value together
for item in dicionary.items():
  print(item)

# can access the keys and values separately
for key, value in dictionary.items():
  print(f"{key}: {value}")


"""
This creates a dictionary that assigns a value to any key that 
does not already exist in the list, in this case it will assign 
an empty list
"""
from collections import defaultdict
my_defaultdict = defaultdict(list)
my_defaultdict[3].append("apple")
"""
This would throw an error in a regular dictionary, but in this case 
it automatically creates an empty list that we can then append 
'apple' to
"""

# combine two separate dictionaries
dict1 = {"color": "red", "size": "large", "type": "ball"}
dict2 = {1: 20, 2: 30}
dict3 = {**dict1, **dict2}

del dict1["color"] # this deletes the "color" key and value
ball_type = dict1.pop("type")  # this deletes "type" from dict1 and also assigns it to the variable ball_type



# --------------------------- upper/lowercase-------------------------------------------------------------------

a = "a"
A = "A"
a.islower() #returns true 
A.isupper()   # returns true 
a.upper()   # sets to uppercase
A.lower()   # sets to lowercase

#---------------------------- Math functions lowercase----------------------------------------------------------
import math

# greatest common divisor 
my_gcd = math.gcd(49,63)

absolute_value = abs(5-13)  # returns absolute value, don't need to import math

# ------------------------------ Binary and bit manipulation -------------------------------------------------- 

fifteen = 15

# Converts integer to binary string with a "0b" prefix
fifteen_to_binary = bin(fifteen)

# Converts binary to integer, it can covert both strings that have a "0b"
# prefix and binary numbers that do not
binary_to_int = int(fifteen_to_binary, 2)

# Converts integer into to binary string witout a "0b" prefix
integer_to_binary = format(fifteen, 'b')


"""
Bit Manipulaion
&  and
|  or
~  not
^  XOR
>>  right shift
<<  left shift
"""

# -------------------------------------- Decorators -----------------------------------------------------------
# these wrap function around another function by using the @symbol above the function

from functools import wraps

def decorator(fn):
  @wraps(fn) #  this helps keep all of the metadata from the original function
  def wrapper(*args, **kwargs): # the wrapper function is acting as your original function
  	# setting result below is needed if your function is returning something
    result = fn(*args, **kwargs)
    print("From the decorator function")
    # this return is only necessary if the orignal function is returning something
    return result
    
  return wrapper
  
@decorator
def add(num1,num2):
  return num1 + num2
  
  
add_sol = add(5,6)
print(add_sol) 

# -------------------------------------- Random --------------------------------------------------------------

# print 5 random integers between 1 and 10
import random

for i in range(5):
  print(random.randint(1,10))

# this imports everything fro the ranom module
# from random import *


#--------------------------------------- Sys -----------------------------------------------------------------

import sys

sys.exit() # this will end a program early


#----------------------------------- Lambda Functions --------------------------------------------------------

# Both of these do the exact same thing
def add(x,y):
  return x + y 
print(add(1,2))

print((lambda x,y: x + y)(1,2))

# another example using list comprehension
lambda_var = (lambda x: [i**2 for i in x])([4,5,6])
print(lambda_var)


#-------------------------------- Asserts --------------------------------------------------------------------

# this will throw an error because the assert_check variable is not equal to 6, 
# the program will crash and "Not large enough" will be printed
assert_check = 5
assert assert_check == 6, "Not large enough"











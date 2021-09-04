# mymodule.py file
def print_odd_numbers(n):
    odd = []
    for i in range(n+1):
        if i%2 != 0:
            odd.append(i)   
    return odd

# import built in modules
# some common built in modules: math, datetime, os, sys, random, statistics, collections, json

# OS Module: This make it possible to perform many operating system tasks. The module in Python provides functions for creating, changing working directory, removing a directory(folder),
#fethcing its contents, changing and identifying the current directoryos

import os
#print(os.mkdir('test_directory')) # This will create a new directory(folder)

#print(os.chdir('test_directory')) # This will change the current directory

print(os.getcwd()) # This will get the current working directory(The folder you are currently working on)

#print(os.rmdir('test_directory'))  # This will remove the directory(The folder)


# Sys Module: This provides functions and variables used to manipulate different parts of the Python runtime environment. 

# Function sys.argv returns a list of command line arguments passed to python script. The item at index[0] in this list is always the name of the script, at index[1] is the argument passed from the command line

#import sys
#print('Welcome {}. Enjoy {} challenge !'.format(sys.argv[0], sys.argv[1]))


from statistics import *

ages = [2,4,6,8,10,10]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))
#print(dir(math)
#print(help(math)

import math
print(help(math))
print(dir(math))

# String Module

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# Random Module

from random import *
print(random()) # it dosent take argument but returns value betw 0 and 0.99
print(randint(1,100)) # This return random integer number
print(help(random))

from random import *
print(random_user_id())

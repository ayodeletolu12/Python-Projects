# day 4 of 30 days of python challenge

# string concantenation

firstname = 'Michelle'
lastname = 'Olorunfemi'
print('get the full name and display on the screen', firstname + ' ' + lastname)
print("I hope everyone is enjoying the 30 days of python challenge \nAren't they?")
print('Days\tTopics\tExercises')
#print('Days\t14Topics\t5Exercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')

# string formating

print('Another way to display the full name is. My full name is {} {}'.format(firstname, lastname))

# Multiplication table

print('{} * {} = {}'.format(2, 1, 2*1))
print('{} * {} = {}'.format(2, 2, 2*2))
print('{} * {} = {}'.format(2, 3, 2*3))
print('{} * {} = {}'.format(2, 4, 2*4))
print('{} * {} = {}'.format(2, 5, 2*5))
print('{} * {} = {}'.format(2, 6, 2*6))
print('{} * {} = {}'.format(2, 7, 2*7))
print('{} * {} = {}'.format(2, 8, 2*8))
print('{} * {} = {}'.format(2, 9, 2*9))
print('{} * {} = {}'.format(2, 10, 2*10))
print('{} * {} = {}'.format(2, 11, 2*11))
print('{} * {} = {}'.format(2, 12, 2*12))

# string interpolation, using the f-strings to inject the data into the coresponding positions

a = 4
b = 3
print(f'{a} + {b} = {a + b}')

# python strings as sequences of characters
# The simplest way to extract characters from strings and individual members from any sequence is to unpack them into corresponding variables

language = 'python'
a,b,c,d,e,f = language
print(a)
print(b)

# Accessing characters in strings by index

language = 'python'
print(language[0])
print(language[len(language)-1]) # this gets the n ,..     ,
print(language[len(language)-2]) # this gets the o

# slicing python strings: we can slice strings into sub strings.

word1 = 'congratulations'
print(word1[0:7]) # this will slice congrat
print(word1[3:14])

# String methods
# capitalize() this capitalize the first character in a word

myfullname = 'tolulope olorunfemi'
print(myfullname.capitalize())
print(myfullname.upper())
print(myfullname.count('o'))
print(myfullname.split())
print(myfullname.title())
print(myfullname.endswith('e'))

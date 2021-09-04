# Exercise 3
# Get two numbers from the user using input prompt. if a is greater than b return a is greater than b, if a is less than b return a is smaller than b, else a is equal to b

a = int(input('Enter the first value to compare: '))
b = int(input('Enter the second value to compare: '))
if a > b :
    print("Please note that the first value is greater than the second valuei.e a > b")
elif a < b :
    print("Please note that the second value is greater than the first value i.e b > a")
else:
    print('Wow great to know that both values are the same ')

# Day 9 Conditional

#Exercises: Get user input using input('Enter your age: '). if user is 18 or older, givefeedback: You are old enough to drive.
#if below 18 give feedback to wait for the missing amount of years,

#Output should look like this
#Enter your age: 30
#You are old enough to lear to drive
#Output:
#Enter your age: 15 you need 3 more years to learn to drive

user_firstname = input('Enter your first name: ').capitalize()
age = int(input('Enter your age: '))
if type(user_firstname) == str:
    if age > 18 or age == 18:
        print(f'Hello {user_firstname}, your age is {age}, trust me you are old enough to learn to drive')
    else:
        output = 18 - age
        print(f'Hello {user_firstname}, your age is {age}, trust you still have {output} substantial years more to learn to drive')
else:
    print('Kindly enter a valid first name')

# This function add 2 numbers togethe and return the value to the console
# This program requests user to input their numbers from the keyboard

num1 = int(input("Enter the first number you want to add together"))
num2 = int(input("Enter the second number you want to add together"))

def Add(num1, num2) :
    answer = (num1 + num2)
    print("The addition of this two values ", num1, num2, answer)
    
Add(num1, num2)    

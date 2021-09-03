# This function subtracts 2 numbers from each other and return the value to the console
# This program requests user to input their numbers from the keyboard

num1 = float(input("Enter the number you want to subtract from: "))
num2 = float(input("Enter the the number you want to remove: "))

def subtr(num1, num2) :
    answer = (num1 - num2)
    print("The subtraction of these two values ", num1, "and", num2, "is",  answer)

subtr(num1, num2)

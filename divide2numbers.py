# This function divides 2 numbers and return the value to the console
# This program requests user to input their numbers from the keyboard

num1 = float(input("Enter the 1st number you want to divide: "))
num2 = float(input("Enter the 2nd number: "))

def div(num1, num2) :
    answer = (num1 / num2)
    print("The division of these two values ", num1, "and", num2, "is",  answer)

div(num1, num2)

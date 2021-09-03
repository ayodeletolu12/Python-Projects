# This function gets the floor division of different 2 values and return the value to the console
# This program requests user to input their numbers from the keyboard

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))


def FloorDiv(num1, num2) :
    answer = (num1 // num2)
    print("The Floor division of these two values ", num1, "and", num2, "is", answer)
    
FloorDiv(num1, num2)

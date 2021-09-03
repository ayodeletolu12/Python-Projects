# This function get the remainder of 2 values and return the value to the console
# This program requests user to input their numbers from the keyboard

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number you want to get the remainder: "))



def Mod(num1, num2) :
    answer = (num1 % num2)
    print("The remander of this two values ", num1, "and", num2, "is", answer)
    
Mod(num1, num2)

# This function computes a number raised to a power. That is exponential and return the value to the console
# This program requests user to input their numbers from the keyboard

num1 = float(input("Enter the base number or exponential: "))
num2 = float(input("Enter the power that you want to raise the base number to: "))


def Exp(num1, num2) :
    answer = (num1 ** num2)
    print("The exponential of this two values ", num1, "and", num2, "is", answer)
    
Exp(num1, num2)



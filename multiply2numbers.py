# This function multiply 2 numbers together and return the value to the console
# This program requests user to input their numbers from the keyboard

num1 = float(input("Enter the 1st number you want to multiply: "))
num2 = float(input("Enter the 2nd number you want to multiply: "))

def mult(num1, num2) :
    answer = (num1 * num2)
    print("The multiplication of these two values ", num1, "and", num2, "is",  answer)

mult(num1, num2)


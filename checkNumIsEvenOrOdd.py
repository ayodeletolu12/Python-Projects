# How to check that a number is even or odd

# This script is a function that will request for user input, the program will check the number entered by the user and confirm if its even or odd

num = int(input("Kindly enter the number you want to check if its even or odd: "))

def checkEvenOrOdd(num) :
    if num % 2 == 0 :
        print(f"Please note that the number you just entered {num} has been confirmed to be an EVEN NUMBER")
    else :
         print(f"Please note that the number you just entered {num} has been confirmed to be an ODD NUMBER")

checkEvenOrOdd(num)





try:
    my_name = input('Enter your name please? ').capitalize()
    my_age = int(input("Enter your age "))
    new_age = my_age + 20
    print(f" Hello {my_name} your new age is {new_age}")
except:
    print("Something went wrong")
    

# The following list contains some fruits
# fruits = ['banana','orange','mango','lemon','apple']

#if a fruit doesn't exist in the list, add the fruit to the list and print the modified list
# if the fruit exists print('That fruit already exist in the list')

fruits = ['banana','orange','mango','lemon','apple']

fruit = input("Enter any fruit of your choice to check if it exists in the list of fruits in the store: ").lower()

if fruit not in fruits:
    fruits.append(fruit)
    print("The fruits you just entered doesn't exist in the list, the system will add it to the list of fruits", fruits)
else:
    print('That fruit already exist in the list')
    

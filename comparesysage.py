# This exercise compares the values of my_age and the age declared by the system

system_age = 40
your_age = int(input("Enter your age: "))
if system_age == your_age or system_age > your_age:
    age_diff = system_age - your_age
    if age_diff == 0:
        print(f'System age is {system_age} and your age is {your_age}, trust me, you share the same age as the system age')
    elif age_diff == 1:
        print(f'System age is {system_age} and your age is {your_age}, trust me the system is {age_diff} year older than you')
    elif age_diff > 1:
        print(f'system age is {system_age} and your age is {your_age}, trust me I am {age_diff} years older than you')
else:
    print(f'system age is {system_age} and your age is {your_age}, trust me you are simply older than the system age')
         

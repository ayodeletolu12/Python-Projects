def addition():
    x =150
    y =100
    total1 = x+y
    return total1
    
addition()

mult = 2 * addition()
print(mult)


def addition(x, y):
    total2 = x+y
    return total2
    
print(addition(100,200))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
sum_of_numbers(10)
sum_of_numbers(100)
sum_of_numbers(1000)
    
# function to calculate employees / applicant age

def calc_user_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ',calc_user_age(2021,1998))

# function to calculate the weight of an object in Newton

def weight_of_obj(mass, gravity):
    weight = str(mass * gravity) + 'N'
    return weight
print('The weight of an object is: ', weight_of_obj(20,9.8))

# passing argument with keys and values

def print_full_name(firstname, lastname):
    fullname = firstname + ' ' + lastname
    return fullname
print(print_full_name(firstname ='Tolulope', lastname='Olorunfemi'))

# function to print list of even numbers for a range of numbers

def print_even_numbers(n):
    even = []
    for i in range(n+1):
        if i%2 == 0:
            even.append(i)   
    return even 
           
print(print_even_numbers(10))            


# function to print list of odd numbers for a range of numbers

def print_odd_numbers(n):
    odd = []
    for i in range(n+1):
        if i%2 != 0:
            odd.append(i)   
    return odd 
           
print(print_odd_numbers(10))

# funtions to add arbitrary numbers

def sum_of_num(*args):
    total = 0
    for i in args:
        total+=i
    return total
print(sum_of_num(5,6,8,10))
    
    
    

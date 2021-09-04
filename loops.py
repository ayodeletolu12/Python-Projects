# while loop

count = 0
while count < 5:
    count += 1
    print(count)

count = 0
while count < 5:
    print(count)
    count +=1
else:
    print(count)

count = 0
while count < 5:
    print(count)
    count+=1
    if count == 3:
       break
    
# for loop

letters = 'python is a programming language'

for letter in letters:
    print(list(letter))

# for loop in dictionary

student = {
    'firstname':'Tolulope',
    'lastname':'Olorunfemi',
    'gender':'Female',
    'country':'Nigeria',
    'city':'Lagos',
    'age' : 45,
    'is_married': True,
    'skills':['Javascript', 'CSS', 'HTML', 'Python', 'WIndows Server Administration'],
    'address': {
        'street':'10 Church Street Aina Ajayi Estate Omoleye Bus Stop Ile Iwe Abule Egba Lagos',
        'zip code':'101001'
        }
    }
for keys in student:
    print(keys)

for keys, values in student.items():
    print(keys,values)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1)if number !=5 else print("loop's ended")

#    for key in student:
 #       if key == 'skills':
 #           for skill in student['skills']:
  #              print(skill)

# add keys and values to an empty created dictionary
dog = {}
print(dog)
dog['color'] = ['black']
dog['legs'] = [2]
dog['age'] = [10]
print(dog)

#create a student dictionary and add firstname, lastname, gender, age, marital_status, skills, country, city and address as keys for the dictionary

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

#get the length
print('The length of the dictionary(student) is', len(student))

# get the value of skills and check the data type

print('The value of the student skill is', student.get('skills'), 'The data type of value skills is', type(student.get('skills')))

# Modify the skills values by adding one or two skills
# dict_name[keys].append('values') will add value to a key in a dictionary

student['skills'].append('cloud Technology')
student['skills'].append('DevOps')
student['skills'].append('Web developemnt')
print('The new skills for the student is', student.get('skills'))

#get the dictionary keys and values as a list

print('The student keys are listed as follow', student.keys())
print('The student values are listed as follow', student.values())


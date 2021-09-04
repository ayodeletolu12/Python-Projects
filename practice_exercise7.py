# Here we have a person Dictionary
# person = {
#    'firstname':'Tolulope',
#    'lastname':'Olorunfemi',
#    'gender':'Female',
#    'country':'Nigeria',
#    'city':'Lagos',
#    'age' : 45,
#    'is_married': True,
#    'skills':['Javascript', 'React', 'CSS', 'HTML', 'Python', 'Node', 'MongoDB', 'WIndows Server Administration'],
#    'address': {
#        'street':'10 Church Street Aina Ajayi Estate Omoleye Bus Stop Ile Iwe Abule Egba Lagos',
#        'zip code':'101001'
#        }
#    }
# 1. check if the person dictionary has skills key, if so print out the middle skill in the skills list
# 2. check if the person dictionary has skills key, if so check if the person has python skill and print out the result
# 3. if a person skills has only javascript and react, print(he is a front end developer), if the person skills has Node, python, MongoDB, print(he is a backend developer), if the person
# skills has react, Node and MongoDB, print(he is a full stack developer) else print(unknown title)
# 4. if the person is married and if he lives in Lagos, print tyhe information in the following format: Tolulope Olorunfemi lives in Nigeria, He is amrried


# This issue to be revisited

person = {
    'firstname':'Tolulope',
    'lastname':'Olorunfemi',
    'gender':'Male',
    'country':'Nigeria',
    'city':'Lagos',
    'age' : 35,
    'is_married': True,
    'skills':['Javascript', 'React JS', 'CSS', 'HTML', 'Python', 'Node JS', 'MongoDB', 'WIndows Server Administration'],
    'address': {
        'street':'10 Church Street Aina Ajayi Estate Omoleye Bus Stop Ile Iwe Abule Egba Lagos',
        'zip code':'101001'
        }
    }

if 'skills' not in person.keys(): #and 'python' in person['skills']:
    average = int(len(person['skills'])/2)
    print(average)
    print('The middle skill in the list is', person['skills'][average-1 : average+1])
    print(person['skills'])
elif 'Javascript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')
elif 'Node JS' in person['skills']:# and 'Python' in person['skills']:
    print('He is a backend developer')
    

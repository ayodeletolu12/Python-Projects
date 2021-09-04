# To create Dictionary in python, we use the curly bracket {}

person = {
    'firstname':'Tolulope',
    'lastname':'Olorunfemi',
    'country':'Nigeria',
    'age' : 45,
    'is_married': True,
    'skills':['Javascript', 'CSS', 'HTML', 'Python', 'WIndows Server Administration'],
    'address': {
        'street':'10 Church Street Aina Ajayi Estate Omoleye Bus Stop Ile Iwe Abule Egba Lagos',
        'zip code':'101001'
        }
    }

print('The length of this dictionary is', len(person))

# Accessing the Data dictionary
# person['keyitems']

print('The surname of the person is ', person['lastname'].upper())
print('The firstname of the person is', person['firstname'].upper())
print('The country of the person is ', person['country'].upper())
print('The person is ', person['age'],'years old')
print('Is the person married?', person['is_married'])
print('What are the person skilled in?', person['skills'])
print('What is the person street address?', person['address']['street'].upper())

# It is important to note that when accessing keyname that does not exist in a dictionary returns an error. in order to avoid such an error from stoping our program
# we can use the .get() method to get keyitems even though it doesn't exist, it will not not return error but none.

print('The surname of the person is ', person.get('lastname').capitalize())
print('The firstname of the person is', person.get('firstname').capitalize())
print('The country of the person is ', person.get('country').capitalize())
print('The person is ', person.get('age'),'years old')
print('Is the person married?', person.get('is_married'))
print('What are the person skilled in?', person.get('skills'))
print('What is the person street address?', person['address']['street'])
print("The City the person resides is ? Though I don't think its included in the program but lets see the outcome of the execution", person.get('city'))

# Adding items to dictionary

person['language_spoken'] = 'English'
# person['phone'].append('08062906363'): This flags error: key error. I will check later
print(person)

# modifying the dictionary key values

person['firstname'] = 'Michelle'

print('The modified name is now ', person)

# checking keys in a dictionary

print('We need to check if keys are in the dictionary. Is address in the dictionary?', 'address' in person)
print('We need to check if keys are in the dictionary. Is Travelled out in the dictionary?', 'travelled_out' in person)

# Removing keys from dictionary
person.pop('language_spoken')
person.popitem() # this removes the last item
print(person)

# changing Dictionary to a list of items. we use the items() method. person.items()

# clearing a Dictionary: we use the clear() method. print.clear()

# deleting a dictionary e.g del person

# copy dictionary into another we use the copy method. person2 = person.copy()

# getting the dictionary keys as a list. we use the key method e.g keys = person.keys()

keys = person.keys()
print('Thr highlighted keys are?', keys)

# getting the dictionary values as a list. we use the value method e.g values = person.values()

valuess = person.values()
print('The highlighted values are?', valuess)

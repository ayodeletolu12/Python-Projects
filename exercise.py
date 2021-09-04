# File handling
# syntax open('filename', mode)
# mode(r, a, w, x, t, b)
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if the file does not exist
# "w" - Write - Opens a file for writing, creates the file if the file does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode(e.g. images)

# Opening Files for Reading
#The default mode of open is reading. so we do not have to specify 'r' or 'rt'. I have created and saved a file named reading_file_example.txt in the files directory

file = open('testfile', 'w')
file.write('Hello World') 
file.write(' This is our new text file') 
file.write(' and this is another line.') 
file.write(' Why? Because we can.') 
 
file.close() # after opening a file, we should close it

file = open('testfile', 'r')
print(file.read())                    # read(): read the whole text as string, if we want to limit the number of character we read, we can limit it by passing int value to the methods
print(file.readline(), end='')        # readline(): read only the firtst line
print(file.readlines(), end='')       # readlines(): read all the text line by line and returns a list of line


# it is very possible to open a file and forget to close it. to achieve this, we use the with- closes the files by itself

with open('my_test_file', 'w') as file:
    file.write('I am running a python program')
    file.write('I need to check what i wrote')
    
with open('my_test_file', 'a') as file:
    file.write('I am running a python program and I need to append this at the end')
    
with open('my_test_file', 'r') as file:
    print(file.read()) 	    
   
# File with json Extension: json stand for JavaScript Object Notation. it is stringified JavaScript object. This means that you make an object a string by using the " ", ' ' , ''' '''

student_dict = {
        'student_ID': '001',
        'department': 'Computer Science',
        'level': '400L',
        'country': 'Nigeria'
            }

print(student_dict['student_ID'], student_dict['department'])

json_will_now_be = '''{'student_ID': '001', 'department': 'Computer', 'level': '400L', 'country':'Nigeria'}'''

print(json_will_now_be)


# Changing JSON to Dictionary
#to change a JSON to a dictionary, first we import the json module and then we use loads method

import json

json_will_now_be = '''{"student_ID": "001", "department": "Computer", "level": "400L", "country":"Nigeria"}'''

when_changed_back_dict = json.loads(json_will_now_be)

print(when_changed_back_dict)
#print(when_changed_back_dict['student_ID'])


# Changing Dictionary to JSON : we use dumps method from the json module


student_dict = {
        'student_ID': '001',
        'department': 'Computer Science',
        'level': '400L',
        'country': 'Nigeria'
            }
convert_to_json = json.dumps(student_dict)
print(convert_to_json)


#saving JSON FILE

import json
student_dict = {
        'student_ID': '001',
        'department': 'Computer Science',
        'level': '400L',
        'country': 'Nigeria'
            }
with open('test_json_file.json', 'w', encoding='utf-8')as file:
    json.dump(student_dict, file, ensure_ascii=False, indent=4)




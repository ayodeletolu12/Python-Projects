# the first code concatenate the string 'Thirty Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'

# The second code sliced out some texts from the string

# The third code checks if a string is in a particular sentence

# The fourth code replaces the word 'coding' in the string 'Coding For All' to Python

word1 = 'Thirty Days'
word2 = 'Of'
word3 = 'Python'
space = ' '
newWord = word1 + space + word2 + space + word3
print(newWord)

# slice out the first word in a sentence

sentence = 'Coding For All String'
print(sentence[0:6])

# check if a string is in a particular sentence

if 'Coding' in sentence :
    print(True)
else :
    print(False)
    
print(sentence.find('Coding'))

# replace the word 'coding' in the string 'Coding For All' to Python

print(sentence.replace('Coding', 'Python'))

# change Python for Everyone to Python for All using the replace method

print('Python for Everyone'.replace('Everyone', 'All'))

# split string exercise

print(sentence.split())

tech_giant = 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'
print(tech_giant)
print('Facebook'.split())
python_lib = 'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'
print('# ' .join(python_lib))

python_lib2 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
results = '# '.join(python_lib2)
print(results)

# escape sequence

print('I am enjoying this challenge \nI just wonder what is next. ')
print('string'.zfill(34))

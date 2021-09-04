#file = open("trump_speech.txt", "r")

#number_of_lines = 0
#number_of_words = 0
#number_of_characters = 0

#for line in file:
 # line = line.strip("\n")  # won't count \n as character

  #words = line.split() # This will split the line into words
  #number_of_lines += 1
  #number_of_words += len(words)
  #number_of_characters += len(line)

#file.close()

#print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)


file = open('trump_speech.txt', 'r')
data = file.read()
numOfChars = len(data)
numOfWords = len(data.split())
numOfLines = len(data.splitlines())

file.close()


print("lines:", numOfLines, "words:", numOfWords, "characters:", numOfChars)

# Obama speech

file = open('obama_speech.txt', 'r')
data2 = file.read()
numOfChars = len(data2)
numOfWords = len(data2.split())
numOfLines = len(data2.splitlines())

file.close()


print("lines:", numOfLines, "words:", numOfWords, "characters:", numOfChars)

# Melina speech

file = open('melina_speech.txt', 'r')
data3 = file.read()
numOfChars = len(data3)
numOfWords = len(data3.split())
numOfLines = len(data3.splitlines())

file.close()


print("lines:", numOfLines, "words:", numOfWords, "characters:", numOfChars)

# Michelle speech

file = open('michelle_speech.txt', 'r')
data4 = file.read()
numOfChars = len(data4)
numOfWords = len(data4.split())
numOfLines = len(data4.splitlines())

file.close()


print("lines:", numOfLines, "words:", numOfWords, "characters:", numOfChars)

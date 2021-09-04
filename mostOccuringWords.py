# This program produces the most occuring words in the Trump speech

from collections import Counter

file = open('trump_speech.txt', 'r')
speech = file.read()

file.close()
words = speech.split()

counter = Counter(words)

topmostoccuringword = counter.most_common(10)

print("Top 10 most commonly used words in that speech is :", topmostoccuringword)

# This program produces the most occuring words in the Obama speech

from collections import Counter

file = open('obama_speech.txt', 'r')
speech = file.read()

file.close()
words = speech.split()

counter = Counter(words)

topmostoccuringword = counter.most_common(10)

print("Top 10 most commonly used words in that speech is :", topmostoccuringword)


# This program produces the most occuring words in the Melina speech

from collections import Counter

file = open('melina_speech.txt', 'r')
speech = file.read()

file.close()
words = speech.split()

counter = Counter(words)

topmostoccuringword = counter.most_common(10)

print("Top 10 most commonly used words in that speech is :", topmostoccuringword)


# This program produces the most occuring words in the Michelle speech

from collections import Counter

file = open('michelle_speech.txt', 'r')
speech = file.read()

file.close()
words = speech.split()

counter = Counter(words)

topmostoccuringword = counter.most_common(10)

print("Top 10 most commonly used words in that speech is :", topmostoccuringword)


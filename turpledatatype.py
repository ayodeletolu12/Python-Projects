# Tuples
empty_tuple = ()
my_sister = ('Bukola', 'Bunmi', 'Seyi', 'Omolola', 'Kehinde', 'Nicole')
my_brother = ('Taiwo', 'Joshua', 'Godwin')
siblings = my_sister + my_brother
print(siblings)

print('How many siblings do you have? I have just', len(siblings), 'siblings')

# modify tuples

family_members = list(siblings)

family_members.append('Emmanuel')
family_members.append('Olabisi')
print(family_members)

# unpack parents and siblings

*siblings, parents = family_members
print(*siblings)



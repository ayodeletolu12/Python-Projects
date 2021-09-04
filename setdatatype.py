# Set
# difference between union() and update()

item1 = {'Banana', 'Orange', 'Pineaple', 'Pawpaw'}
item2 = {'Rice', 'Beans', 'Gari', 'Banana'}


print(item1.intersection(item2))

#sub and super set issubset() and issuperset

whole_number = {0,1,2,3,4,5,6,7,8,9}
odd_number = {1,3,5,7,9}

print(odd_number.issubset(whole_number))
print(whole_number.issuperset(odd_number))

pyton = {'p','y','t','h','o','n'}
dragn = {'d','r','a','g','o','n'}
print(pyton.issuperset(dragn))

print(pyton.difference(dragn))
print(dragn.difference(pyton))

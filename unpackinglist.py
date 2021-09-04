# unpacking list items

lst = ['item', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)       
print(rest)
print(lst)

# further examples of unpacking list in python.

fruits = ['Mango', 'Banana', 'Guava', 'Orange', 'Apple', 'Citrus', 'Pineaple', 'Pawpaw']
fruit1, fruit2, fruit3, *otherfruits, lastfruit = fruits
print(fruit1)
print(fruit2)
print(fruit3)
print(otherfruits)
print(lastfruit)

# another example

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

# accessing the items in a list

print(fruits[0:])
print(fruits[-10:])
print(fruits[:-1])
print(fruits[-1:])
print(fruits[2:5])
print(fruits[-6:-3])
print(fruits[::-1])

# Adding items to list

lst = []
print(len(lst))
lst.append('Tolu')
lst.append('Yetunde')
lst.append('Michelle')
print(lst)

#inserting items into list

lst.insert(3, 'Mofeoluwa')
lst.insert(4, 'Kinfeoluwa')
print(lst)

# removing item from list

sample_list = []
sample_list.append('jean')
sample_list.append('chinox')
print(sample_list)
sample_list.remove('jean')
print(sample_list)

# removing item using Pop(). pop() method removes the specified index, or the last item if index is not specified

fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

# removing items using del(). it can remove specified index, it can be used to delete items within index range. it can also delete the list completely
# del list[], del list[0], del list[0:4], del list

deleted_items = ['a', 'b', 'c', 'd', 'e']
print(deleted_items)
del deleted_items[0] 
print(deleted_items)
del deleted_items[0:2]
print(deleted_items)
del deleted_items
#print(deleted_items)

# Exercise level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages.sort()) # sorted items
print(ages)
print('Max age = ', ages[-1]) # max age
print('Min age = ',  ages[0]) # min age
print(len(ages))
middle_ages = ages[4] + ages[5]
median_age = middle_ages / 2
print(median_age)
average_age = sum(ages) / len(ages)
print(average_age)
print('The range of ages is ', ages[-1] - ages[0])

# List of Countries

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print('The number of countries in the list is ', len(countries))
# To find middle countries

len_middle_countries = len(countries) // 2 # This will get the length of contries and divided by 2
print(len_middle_countries)
print(countries[len_middle_countries:(len_middle_countries)+2])
print(countries.index('Lesotho'))

# This wil unpack the countries

sub_country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
asia_country, european_country , *scandic = sub_country
print(asia_country)
print(european_country)
print(*scandic)

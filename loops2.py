# iterate 0 to 10 using for loop, do the same using wile loop

count = 0
while count < 11:
    print(count)
    count+=1
    
for count in range(11):
    print(count)

    
# iterate 10 to 0 using for loop, do the same using while loop

count = 11
while count > 0:
    count-=1
    print(count)

for count in range(10,-1,-1):
    print(count)

# write a loop that makes seven calls to print(), so we get on the output the following triangle

for count in range(1,8):
    total ='#' * count 
    print(total)

count = 1
while count < 8:
    total = '#' * count
    count+=1
    print(total)

for count in range(1,9):
    total  = '#' * 8
    print(total)

count = 1
while count < 9:
    total = '#' * 8
    count+=1
    print(total)


for count in range(0,11):
    print(f'{count} * {count} =', count*count)

count = 0
while count < 11:
    print(f'{count} * {count} =', count*count)
    count+=1

# iterate through the list, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
# using a for loop and print out items

items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in items:
    print(item)

# use for loop to iterate from 0 to 100 and print only even numbers

for number in range(0,101,2):
    print(number)

# use for loop to iterate from 0 to 100 and print only odd numbers

for number in range(1,100,2):
    print(number)

# use for loop to iterate from 0 to 100 and print the sum of numbers answer must be 5050

total = 0
for number in range(0,101):
    total = total + number
print(total)

count = 0
total = 0
while count < 101:
    total = total +count
    count+=1
print(total)
    
# use for loop to iterate from 0 to 100 and print the sum of all even numbers and odd numbers answers must be 2550 for even and 2500 for odd

total = 0
for number in range(0,101, 2):
    total = total + number
print('sum of even numbers from 0 to 101 is: ', total)

total = 0
for number in range(1,100, 2):
    total = total + number
print('sum of odd numbers from 0 to 10 is: ', total)


# loop through the countries and extract all the countries containing the word land

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
];
for country in countries:
    if 'land' in country:
        print(country)
        
# use loop to reverse the order fruit list, ['banana','orange','mango','lemon']

fruit_list = ['banana','orange','mango','lemon']
for fruit in fruit_list:
    length = len(fruit_list)
    fruit_list[-1] = fruit
    print(fruit)

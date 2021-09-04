# scripts that calculate the number of second, minutes, hours, days, months a person has lived

number_of_years = int(input('Enter the number of years you have lived: '))
number_of_months = number_of_years * 12
number_of_weeks = number_of_years * 52
number_of_days = number_of_years * 365
number_of_hours = number_of_days * 24
number_of_minutes = number_of_hours * 60
number_of_seconds = number_of_minutes * 60
print('Number of years you have lived: ', number_of_years,'yr(s)')
print('Number of month you have lived: ', number_of_months, 'mths')
print('Number of weeks you have lived: ', number_of_weeks, 'wks')
print('Number of days you have lived: ', number_of_days, 'dys')
print('Number of hours you have lived: ', number_of_hours, 'hrs')
print('Number of minutes you have lived: ', number_of_minutes,'mins')
print('Number of seconds you have lived: ', number_of_seconds,'secs')

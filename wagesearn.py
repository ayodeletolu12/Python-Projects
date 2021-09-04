# Script that prompts the user to enter hours and rate per hour to calculate pay of the person provided he worked everyday, every week every month

hours = int(input('Enter hours worked in a day: '))
rate_per_hour = int(input('Enter your rate per hour: '))
daily_earning = hours * rate_per_hour
weekly_earning = daily_earning * 5
monthly_earning = weekly_earning * 4
yearly_earning = monthly_earning * 12
print(f'My daily earning if I worked {hours} hours with {rate_per_hour} $ is: $',daily_earning)
print('My weekly earning is: $',weekly_earning)
print('My monthly earning is: $',monthly_earning)
print('My yearly earning is: $',yearly_earning)

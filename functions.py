# function to calcute area of circle PI * r * r

def area_of_circle(radius, PI= 9.8):
    area = int(PI * radius**2)
    return area
print(area_of_circle(10))

# function to add all arbitary numbers

def sum_all_numbers(*nums):
    total = 0
    for num in nums:
        if type(num) == int:
            total = total + num
            print(f'Yes, {num} is a number')
    return total
    
print('The sum of all the numbers in the list is: ', sum_all_numbers(10,10,10,10,10,'k'))

#function to convert temperature in centegrade to farenheit using F = (C * 9/5)+32

def centegrade_to_farenheit(n):
    farenheit = (n * 9/5) + 32
    return farenheit
print('coverting from centigrade to farenheit: ', centegrade_to_farenheit(1))


def check_season(season_month):
    if season_month == 'September' or season_month == 'October' or season_month == 'November' :
        print(f"Thanks for the input, I understand you want to know the season the month belongs to. You have entered {season_month}, and the month belongs to an 'AUTUMN' season")
    elif season_month == 'December' or season_month == 'January' or season_month == 'February' :
        print(f"Thanks for the input, I understand you want to know the season the month belongs to. You have entered {season_month}, and the month belongs to a 'WINTER' season")
    elif season_month == 'March' or season_month == 'April' or season_month == 'May' :
        print(f"Thanks for the input, I understand you want to know the season the month belongs to. You have entered {season_month}, and the month belongs to a 'SPRING' season")
    elif season_month == 'June' or season_month == 'July' or season_month == 'August' :
        print(f"Thanks for the input, I understand you want to know the season the month belongs to. You have entered {season_month}, and the month belongs to a 'SUMMER' season")
    else :
        print('Invalid month. kindly enter the correct month')
check_season(input('Enter the month you want to confirm the season: ').capitalize())

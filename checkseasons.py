#Check if the season is Autumn, Winter, Spring or Summer. if the user input is: September, October or Novemeber, the season is Autumn. December, January, or February, the season is Winter.
#March, April or May, the season is Spring June, July or August, the season is Summer

# September, October or Novemeber, the season is Autumn

# December, January, or February, the season is Winter

# March, April or May, the season is Spring

# June, July or August, the season is Summer

season_month = input('Enter a month in the year to know which season the month belongs to: ').capitalize()

if season_month == 'September' or season_month == 'October' or season_month == 'November' :
    print(f"Thanks for the input, I understand you want to know the season the month belongs to. You have entered {season_month}, and the month belongs to 'AUTUMN'")
elif season_month == 'December' or season_month == 'January' or season_month == 'February' :
    print(f"Thanks for the input, I understand you want to know the season the month belongs to. You have entered {season_month}, and the month belongs to 'WINTER'")
elif season_month == 'March' or season_month == 'April' or season_month == 'May' :
    print(f"Thanks for the input, I understand you want to know the season the month belongs to. You have entered {season_month}, and the month belongs to 'SPRING'")
elif season_month == 'June' or season_month == 'July' or season_month == 'August' :
    print(f"Thanks for the input, I understand you want to know the season the month belongs to. You have entered {season_month}, and the month belongs to 'SUMMER'")
else :
    print('Invalid month. kindly enter the correct month')

    

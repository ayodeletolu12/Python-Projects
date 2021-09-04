#3 Script that prompts the user to enter side a, side b and side c of a triangle and calculate the perimeter of that triangle: The formular: a+b+c

sideA_of_triangle = float(input('Kindly enter the sideA of the triangle without the unit: '))
sideB_of_triangle = float(input('Kindly enter the sideB of the triangle without the unit: '))
sideC_of_triangle = float(input('Kindly enter the sideC of the triangle without the unit: '))
perimeter_of_triangle = sideA_of_triangle + sideB_of_triangle + sideC_of_triangle
print('The perimeter of the triangle is: ', perimeter_of_triangle, 'UNIT')


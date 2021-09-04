# Write a code which gives grade to students according to their scores
# In the program, I am making use of the range() inbuilt function to perform the task

#80 - 100, A
#70-79, B
#60-69, C
#50-59, D
#0-49, F

student_score = int(input('Kindly enter your score to confirm your grade: '))

if student_score in range(80,101) :
    print(f'Excelent!!!. Your score is {student_score}. You have Grade A')
elif student_score in range(70,80) :
    print(f'Good!!. Your score is {student_score}. You have Grade B')
elif student_score in range(60,70) :
    print(f'Credit!. Your score is {student_score}. You have Grade C')
elif student_score in range(50,60) :
    print(f'Fair!. Your score is {student_score}. You have Grade D')
elif student_score in range(0,50) :
    print(f'Poor!. Your score is {student_score}. You have Grade F')
else :
    print('Sorry, you have entered an invalid score. check again and re-enter your score')

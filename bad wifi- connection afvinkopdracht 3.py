print('Reboot the compute and try to connenct. ')
problem = input('Did that fix the problem?: ')
if problem == 'yes' :
    print('Einde')
elif problem == 'no' :
    print('Reboot the compute and try to connenct.')

problem_2 = input('Did that fix the problem?: ')
if problem_2 == 'yes':
    print('Einde')

elif problem_2 == 'no':
    print('Make sure the cables between the router & modem are plugged in firmly')


problem_3 = input('Did that fix the problem?: ')
if problem_3 == 'yes':
    print('Einde')

elif problem_3 == 'no':
    print('Move the router to a new location and try to connect.')
    
problem_4 = input('Did that fix the problem?: ')
if problem_4 == 'yes':
    print('Einde')

elif problem_4 == 'no':
    print('Get a new router')

print('einde')

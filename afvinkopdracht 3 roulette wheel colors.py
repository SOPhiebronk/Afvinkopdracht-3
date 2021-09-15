number = int(input('Enter a pocket number: '))

if number == 0:
    print('The pocket is green')
elif number <= 10:
    if number%2==0:
        print('The pocket is Black')
    else:
        print('The pocket is Red')
elif number <= 18 or 11:
    if number%2==0:
        print('The pocket is Red')
    else:
        print('The pocket is Black')
    
elif number <= 28 or 19:
    if number%2==0:
        print('The pocket is Black')
    else:
        print('The pocket is Red')
        
elif number <= 36 or 29:
    if number%2==0:
        print('The pocket is Red')
    else:
        print('The pocket is Black')

elif number > 36:
    if number%2==0:
        print('Error')
    else:
        print('Error')
   

#het laatste onderdeel doet het niet     
        

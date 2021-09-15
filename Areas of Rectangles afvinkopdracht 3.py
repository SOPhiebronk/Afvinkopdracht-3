rectangle_1_length = int(input('Enter the length of rectangle 1: '))
rectangle_1_width = int(input('Enter the width of rectangle 1: '))

rectangle_2_length = int(input('Enter the length of rectangle 2: '))
rectangle_2_width = int(input('Enter the width of rectangle 2: '))

Area_1 = (rectangle_1_length * rectangle_1_width)
Area_2 = (rectangle_2_length * rectangle_2_width)

if Area_1 == Area_2:
    print('The areas are the same')
if Area_1 > Area_2:
    print('Area 1 is greater')
if Area_2 > Area_1:
    print('Area 2 is greater')

    

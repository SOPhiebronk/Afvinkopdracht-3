vegetarian = str(input('Is anyone in your party a vegetarian?: '))
vegan = str(input('Is anyone in your party a Vegan?: '))
gluten_free = str(input('Is anyone in your party gluten-free?: '))
print('Here are your restaurant choices: ')
if vegetarian == 'no' and vegan=='no'and gluten_free =='no':
    print('Joes Gourmet Burgers')
if vegetarian == 'yes' and vegan=='no'and gluten_free =='no':
    print('Main Street Pizza Company')
if vegetarian == 'yes' and vegan=='yes' and gluten_free =='yes':
    print('Corner Café')
if vegetarian == 'yes' and vegan=='no' and gluten_free =='no':
    print('Mamas Fine Italian')
if vegetarian =='yes' and vegan=='yes' and gluten_free =='yes':
    print('The Chefs Kitchen')



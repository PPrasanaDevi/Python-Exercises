# Design a program to enter the user names of two primary colors to mix and
# Display the color you get after mixing.

color1 = input('Enter one primary color: ')
color2 = input('Enter second primary color: ')

if color1 == 'red' and color2 == 'blue':
    print('You get Purple')
elif color1 == 'blue' and color2 == 'red':
    print('You get purple')
elif color1== 'red' and color2 == 'yellow':
    print('You get Orange')
elif color1== 'yellow' and color2 == 'red':
    print('You get Orange')
elif color1== 'blue' and color2 == 'yellow':
    print('You get green')
elif color1== 'yellow' and color2 == 'blue':
    print('You get green')
else:
    print('ERROR: The color you entered is not a primary color')

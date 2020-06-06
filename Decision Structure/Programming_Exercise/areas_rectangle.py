#Find area of two rectangle.
#Tell the user which rectangle has the  greater areas or if the areas are the same.

# Get length of the first rectangle
length1 = float(input('Enter length for first rectangle: '))
#Get width of the first rectangle
width1 = float(input('Enter the width for the second rectangle: '))

#Calculat area for first rectangle.
area1 = length1 * width1

# Get length of the second rectangle
length2 = float(input('Enter length for second rectangle: '))
#Get width of the second rectangle
width2 = float(input('Enter the width for the second rectangle: '))

#Calculat area for second rectangle.
area2 = length2 * width2

#Determine which rectangle is greater or if they are equal
if area1 > area2:
    print('Area 1 is greater')
elif area2 > area1:
    print('Area 2 is greater')
else:
    print('Both are same')

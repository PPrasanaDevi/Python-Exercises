#write a program that asks the user for a number in the range 1 through 7.
#The program display the corresponding day of the week.

#Get a number from the user
number = int(input('Enter a number from 1 through 7: '))

if number == 1:
    print('Monday')
elif number == 2:
    print('Tuesday')
elif number == 3:
    print('Wednesday')
elif number == 4:
    print('Thursday')
elif number == 5:
    print('Friday')
elif number == 6:
    print('Saturday')
elif number == 7:
    print('Sunday')
else:
    print('ERROR: You have entered a wrong number!!!')

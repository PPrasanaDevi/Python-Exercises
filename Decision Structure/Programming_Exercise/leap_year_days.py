#Get the year from the user to find leap year

year = int(input('Enter the year: '))

if year % 4 ==0 and year % 100 !=0 or year % 400 ==0:
    print(year,' is leap year and has 29 days.')
        
else:
    print(year, 'is not a leap year and has 28 days')
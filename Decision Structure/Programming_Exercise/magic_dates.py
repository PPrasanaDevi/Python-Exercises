#Get the month, day and two digit year from the user

month = int(input('Enter the month in numeric form: '))

day = int(input('Enter the day: '))

year = int(input('Enter the two digit year: '))

magic_date = month * day

if magic_date == year:
    print('Date is a magic date')
else:
    print('Date is not a magic date')

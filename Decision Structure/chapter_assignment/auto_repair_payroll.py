#Named constants to represent the base hours and the overtime multiplier.

BASE_HOURS = 40
OT_MULTIPLIER = 1.5

#Get the hours worked and the hourly pay rate
hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

#Calculate and display gross pay
if hours > BASE_HOURS:
    #Calculate the gross pay with overtime
    #Get the overtime hours
    overtime_hours = hours - BASE_HOURS

    #calculate the amount of overtime pay
    overtime_pay = overtime_hours *pay_rate *OT_MULTIPLIER

    #Gross pay
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    #Calculate the gross pay without overtime
    gross_pay = hours * pay_rate
#Display the gross pay
print('The gross pay is $', format(gross_pay, ',.2f'),sep='')

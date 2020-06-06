#Program that asks the user to enter packages number
#Calculate the discount amount and display
#Packages retail for $99
discount_amount = 0.0
number_of_packages = int(input('Enter number of packages:'))

if number_of_packages > 10 and number_of_packages < 19:
    discount_amount = (99 *10)/100 #10% discount
    print('Discount amount: ', discount_amount)
elif number_of_packages > 20 and number_of_packages < 49:
    discount_amount = (99*20)/100 # 20% discount
    print('Discount amount: ', discount_amount)
elif number_of_packages > 50 and number_of_packages < 99:
    discount_amount = (99*30)/100 #30% discount
    print('Discount amount: ', discount_amount)
elif number_of_packages >= 100:
    discount_amount =(99*40)/100 #40% discount
    print('Discount amount: ', discount_amount)
else:
    print('Invalid number')

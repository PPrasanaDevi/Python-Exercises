#This program calculates retail prices.

MARK_UP = 2.5
another ='y' #variable to control the loop.

#Process one or more items.
while another =='Y' or another == 'y':
    #Get the item's wholesale cost.
    wholesale = float(input("Enter the item's" + "wholesale cost":))

    #Validate the wholesale cost.
    while wholesale < 0:
        print('ERROR: the cost cannot be negative.')
        wholesale = float(input("Enter the item's" + "wholesale cost":))

    #Calculate the retail price.
    retail = wholesale *MARK_UP

    #Display the retail price.
    print('Retail price: $', format(retail, ',.2f'), sep ='')

    #Do this again?
    another = input('Do you have another item?' + '(Enter Y for yes):')
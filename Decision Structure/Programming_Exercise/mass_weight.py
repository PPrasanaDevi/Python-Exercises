#Calculate the weight of an object in newtons.

#Get the mass of the object.
mass = float(input('Enter the mass of the object: '))

#Calculate its weight.
weight = mass * 9.8

print('Weight = ',weight ,'newtons')

if weight > 500:
    print('The object is too heavy')
elif weight < 100:
    print('The object is too light')


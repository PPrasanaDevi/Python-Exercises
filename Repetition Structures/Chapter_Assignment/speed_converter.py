#This program converts the speeds 60kph through 130kph( in 10 kph increments) to mph.

START_SPEED = 60
END_SPEED = 131
INCREMENT =10
CONVERSION_FACTOR = 0.6214

#PRINT TABLE HEADINGS
print ('KPH\tMPH')
print('----------')


#print the speeds.
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, '\t', format(mph, '.1f'))

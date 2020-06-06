#This program uses a loop to display a table the numbers 1 through 10 and their
#squares.

#print the table headings.
print('Number\tSquares')
print('---------------------')

#print the numbers 1 through 10 and their squares.
for number in range(1,11):
    square = number * 2
    print(number, '\t', square)

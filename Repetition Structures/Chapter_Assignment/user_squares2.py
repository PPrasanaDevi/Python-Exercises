#This program uses a loop to display a table of numbers and their squares.

#Get the starting value.
print('This program displays a list of numbers')
print('and their squares')
start = int(input('Enter the starting number: '))

#Get the ending limit.
end = int(input('How high should I go?'))

#print the table headings.
print()
print('Numbers\tSquares')
print('----------------')

#print the numbers and their squares.
for number in range(start, end + 1):
    square = number **2
    print(number,'\t',square)

#This program gers three test scores and displays their average.
#It congrtulates the user if the average score is high score.

#The HIGH_SCORE named constant holds the value that is considered as high score.
HIGH_SCORE = 95

#Get the three test scores
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

#calculate the average
average = (test1 + test2 + test3)/3

#print the average
print('The average score is',format(average,'.2f'))

#if the average score is high congratulate the user.
if average >= HIGH_SCORE:
    print('Congratulations!!')
    print('That is a great score')
else:
    print('Better luck next time')

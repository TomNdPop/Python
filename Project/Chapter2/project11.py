#asking user for the males and females
males = float(input('Enter the number of males: '))
females = float(input('Enter the number of females: '))

#calculating total and percentages
total = float(males+females)
males = males/total
females = females/total

# printing in fields
print('The total number of females is: ',format(females, '%'))
print('The total number of males is: ',format(males, '%'))

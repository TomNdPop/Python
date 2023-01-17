# declaring the three tests
test1 = float(input('What was your first test score?'))
test2 = float(input('What was your second test score?'))
test3 = float(input('What was your third test score?'))

# Calculating the total overall score
total = (test1+test2+test3)
average = total/3

# printing the total
print('The average is: ',average)
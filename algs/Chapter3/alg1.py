#Asking user to input a float value into x
x = float(input('Enter a float value and I might spit out y and z for you: '))

#if statement and print statements
if x > 100.:
    y=20
    z=40
    print('Fine, y = ',format(y,',.2f'),'z = ',format(z,',.2f'))
else: print('You worthless muggle.')
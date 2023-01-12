#Asking for tip, salestax,and subtotal
sub = float(input('Subtotal: '))
sal= float(input('Sales tax(decimal): '))
tip = float(input('Tip Percentage(decimal): '))

#calculating the total
sub1 = sub*tip
sub2 = sub*sal
total = sub + sub1 + sub2

#printing the total
print('The total is: ', total)

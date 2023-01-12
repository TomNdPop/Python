
#Asking for the five item prices
first = float(input('Enter the price of the first item: '))
second = float(input('Enter the price of the first item: '))
third = float(input('Enter the price of the first item: '))
fourth = float(input('Enter the price of the first item: '))
fifth = float(input('Enter the price of the first item: '))

salesTax = float(input('Please enter the sales tax as a decimal: '))

# Calculating subtotal
subTotal = first+second+third+fourth+fifth

# Calculating Total
total = subTotal + subTotal*salesTax
 # Printing the total
print('The total is:',format(total, ',.2f'))
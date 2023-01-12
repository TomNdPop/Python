# Input for the subtotal
subTotal = float(input('Please enter the subtotal: '))

# Input for the the sales, county sales tax
State = float(input('Please enter the state sales tax as a decimal: '))
County = float(input('Please enter the county sales tax as a decimal: '))

# Calculating the total sales tax
salesTotal = State + County

# Calculating the total
Total = subTotal + subTotal * salesTotal

#Printing the total
print('The total cost after inputting both sales taxes is: ',Total)
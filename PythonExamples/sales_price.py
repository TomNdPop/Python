#Asking for the original price and the discount percent
original = float(input('Please enter the original sales:'))
discount = float(input('Please enter the percentage off (as a decimal):'))

#Calculating the sales_price
discount = original *discount
sale_price = original - discount

#printing the result
print('The sale price is', sale_price)
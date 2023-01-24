#getting the present value, interest rate, and timeframe
present_value = 1000
interest = 0.07
time = int(input('Please Enter the number of years:'))

#Calculating
future_value = present_value*(1+interest)**time

#printing the future value
print('Amount after',time,'years:',format(future_value, ",.2f") )
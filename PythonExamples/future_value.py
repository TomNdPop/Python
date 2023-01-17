#geting the present value, interest rate, and timeframe
future_value = float(input('Enter the desired future amount: '))
interest = float(input('What is the current interest rate?'))
time = float(input('How long do you want to wait?'))

#Calculating
present_value = future_value/(1+interest)**time

#printing the future value
print('You will need to deposit: ',present_value )
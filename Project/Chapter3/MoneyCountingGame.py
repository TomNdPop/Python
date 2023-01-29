#Asking for the number of coins
quar = float(input('How many quarters do you have?'))
dime = float(input('How many dimes do you have?'))
nickels = float(input('How many nickels do you have?'))
peni = float(input('How many pennies do you have?'))

#calculating
quarval = quar*.25
dimeval = dime*.10
nickelval = nickels*.05
pennval = peni*.01

total = quarval + dimeval + nickelval + pennval

#if
if total == 1.00:
    print('Nice Job! You won the DOLLAR GAME.')
elif total > 1.00:
    print('You lost the DOLLAR GAME. You have too much money!')
elif total < 1.00:
    print('You lost the DOLLAR GAME. You do not have enough money.')
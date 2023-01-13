#Calculating jeff's various earnings and debts
#before selling
amountPaid = 2000*40
amountPaidtoBroker = amountPaid*0.03
amountLeftInitial = amountPaid - amountPaidtoBroker
#after selling
amountAfter = 2000*42.75
amountPaidAftertoBroker = amountAfter*.03
amountLeftFinal = amountPaid - amountPaidAftertoBroker
#calculating the total profit or loss
profit = amountLeftFinal - amountLeftInitial

# displaying the various asked quantities
print('The amount paid for the stock was: ',format(amountPaid,'12,.2f'))
print('The amount paid to the broker initially was: ',format(amountPaidtoBroker,'12,.2f'))
print('The amount the stock sold for was: ',format(amountAfter,'12,.2f'))
print('The amount of commision that Joe paid to his broker was: ',format(amountPaidAftertoBroker,'12,.2f'))
print('The amount of profit Joe made was: ',format(profit,'12,.2f'))



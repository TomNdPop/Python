#Initial balance declaration
balance = 0.00

#Opening statements
print('Welcome to the adding machine')
print('Your balance is:', format(balance, ",.2f"))

while True:
    userinput = str(input("Please select an operation: '+','-', or 'Exit': "))
    if (userinput == '+'):
        number = float(input('Please enter a number:'))
        balance = number + balance
        print('Your balance is:', format(balance, ",.2f"))
    if (userinput == '-'):
        number = float(input('Please enter a number:'))
        balance = balance - number
        print('Your balance is:', format(balance, ",.2f"))
    if (userinput == 'Exit'):
        break


         



    
    



 


#Enter User input for some string
choice = input('Enter your decision: ')
#converting the first character in string with string = string[0]

choice = choice[0]
choice = choice.upper()
if choice == 'Y':
    print('Good Choice!')
else:
    print('Bad Choice!')



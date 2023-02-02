total = float(input('Enter your budget amount.'))
while True:
    deficit = input('Enter your expense or EXIT:')
    if deficit == 'EXIT':
        print('Have a great day!')
        if total > 0:
            print('You are under budget. ')
        elif total < 0:
            print('You are over budget. ')
        break
    else:
        deficit = float(deficit)
        total -= deficit
        print(total)



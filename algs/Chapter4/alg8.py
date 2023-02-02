number_valid = False
while not number_valid:
    number = float(input('Input a positive real number. '))
    if number > 0:
        number_valid = True
        print(number)
        print('Well Done!')
    else:
        print('ERROR. I do not eat negativity!')
        
bronco = str(input('Enter your bronco id (enter w):'))

password = str(input('Enter your desired password (must use 8 characters):'))
password_match = str(input('Confirm your password:'))

if (bronco == 'W'):
    print('Please try again! You need more than 8 characters for a strong password!')
else:
    if password == password_match:
        print('These passwords match.')
        print(bronco,password, sep="\n")
    else:
        print('These passwords do not match')

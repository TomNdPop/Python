#Asking for user information
first = str(input('First Name:'))
last = str(input('Last Name:'))
username = str(input('Enter your desired user: '))

#Asking for password
password = str(input('Enter your desired password (must use 8 characters):'))
password_match = str(input('Confirm your password:'))

if len(password) < 8:
    print('Please try again! You need more than 8 characters for a strong password!')
else:
    if password == password_match:
        print('These passwords match.')
        print(first,last,username + "@gmail.com",password, sep="\n")
    else:
        print('These passwords do not match')


age = int(input('Age?'))

if age <= 1:
    print('Toddler')
else:
    if age>1 and age <13:
        print('Child')
    else:
        if age>=13 and age<20:
            print('Teenager')
        else:
            if age>=20:
                print('Adult')
            else:
                print('You are not thinking clearly!')    
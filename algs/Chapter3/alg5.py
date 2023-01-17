#Inputting into the two amount variables
amount1 = float(input('Enter a value greater than 10. '))
amount2 = float(input('Enter a value smaller than 100. '))

#nested if structure
if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2: 
            print('',amount1,' is larger than ',amount2)
        else:
            print('',amount2,' is larger than ',amount1)
    else: 
        print('You are an idiot.')  
else:
    print('You are an idiot.')
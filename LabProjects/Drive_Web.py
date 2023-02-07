#Ryan Lilleyman
#This is the second project for the Spring 2023 semester.
#My lab section is CS - 1110 - 571

#The goal of this project is to
#Ryan Lilleyman
#This is the second project for the Spring 2023 semester.
#My lab section is CS - 1110 - 571

#The goal of this project is to

#Boolean Initialiizng

again_valid = False
d_valid = False
sd_valid = False
scale_valid = False
net_income = 0

#Outside classification valid loop

while not again_valid:
    first_name = input('Enter employee first name: ')
    last_name = input('Enter employee last name: ')
    full_name = first_name + last_name
    hours_worked = input('Enter the number of hours worked in the last week: ')
    print('Enter employee classification:')
    
    while not d_valid:
        division = input('Enter Division: ')
        division = division[0]
        if division in 'ABC':
            d_valid = True
        else:
            d_valid = False
        
    while not sd_valid:
        sub_division = input('Enter Subdivision: ')
        if sub_division in '12':
            sd_valid = True
        else:
            sd_valid = False

    while not scale_valid:
        scale = input('Enter Scale: ')
        if scale in 'abc':
            scale_valid = True
        else:
            scale_valid = False

    classification = division + sub_division + scale

    if division =='A':
        if sub_division ==1:
            if scale =='a':
                if hours_worked <= 40:
                    net_income = hours_worked * 10.75
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *10.75
            elif scale =='b':
                if hours_worked <= 40:
                    net_income = hours_worked *12.50
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *12.50
            elif scale =='c':
                if hours_worked <= 40:
                    net_income = hours_worked *14.50
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *14.50

        if sub_division ==2:
            if scale =='a':
                if hours_worked <= 40:
                    net_income = hours_worked *11.75
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *11.75
            elif scale =='b':
                if hours_worked <= 40:
                    net_income = hours_worked *14.50
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *14.50
            elif scale =='c':
                if hours_worked <= 40:
                    net_income = hours_worked *17.50
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *17.50
                    
    elif division =='B':
        if sub_division ==1:
            if scale =='a':
                if hours_worked <= 40:
                    net_income = hours_worked *13.00
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *13.00
            elif scale =='b':
                if hours_worked <= 40:
                    net_income = hours_worked *16.00
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *16.00
            elif scale =='c':
                if hours_worked <= 40:
                    net_income = hours_worked *18.50
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *18.50

        if sub_division ==2:  
            if scale =='a':
                if hours_worked <= 40:
                    net_income = hours_worked *15.00
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *15.00
            elif scale =='b':
                if hours_worked <= 40:
                    net_income = hours_worked *18.50
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *18.50
            elif scale =='c':
                if hours_worked <= 40:
                    net_income = hours_worked *22.00
                else:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *22.00

    elif division =='C':   
        if sub_division ==2:
            if scale =='a':
                if hours_worked <= 40:
                    net_income = hours_worked *16.75
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *16.75
            elif scale =='b':
                if hours_worked <= 40:
                    net_income = hours_worked *18.50
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *18.50
            elif scale =='c':
                if hours_worked <= 40:
                    net_income = hours_worked *20.50
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *20.50

        if sub_division ==1:
            if scale =='a':
                if hours_worked <= 40:
                    net_income = hours_worked *19.25
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *19.25
            elif scale =='b':
                if hours_worked <= 40:
                    net_income = hours_worked *25.00
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *25.00
            elif scale =='c':
                if hours_worked <= 40:
                    net_income = hours_worked *30.00
                elif hours_worked > 40:
                    hour_excess = (hours_worked - 40) * 1.5
                    net_income = (hours_worked + hour_excess) *30.00
    again = str(input("Do you want to enter another employee?"))
    again = again[0]
    again = again.upper()    
    if again in 'Y':
        again_valid==False
    elif again in 'N':
        again_valid==True
    else:
        again_valid==True
    print(f"Employee Name: {full_name}")
    print('Employee Classification:',classification)
    print('Total Pay:', format(net_income,',.2f'))

# Ryan Lilleyman
# This is the second project for the Spring 2023 semester.
# My lab section is CS - 1110 - 571

# The goal of this project is to apply the concepts of input validation, 
# condition - controlled loops, and decision structures. We will use these concepts to create 
# program that takes in inputs and outputs employee information.

again_valid = False
net_income = 0
pay_rate = 0

# Outside classification valid loop
while not again_valid:

    scale_valid = False

    #inputs
    first_name = input('Enter employee first name: ')
    last_name = input('Enter employee last name: ')
    full_name = first_name + " " + last_name

    hours_worked = float(input('Enter the number of hours worked in the last week: '))
    while hours_worked < 0:
        hours_worked = float(input('Enter the number of hours worked in the last week: '))

    #division validation
    division: str = input('Enter Division: ')
    while division[0] not in 'ABC':
        division: str = input('Enter Division: ')

    #sub_division validation
    sub_division = input('Enter Subdivision: ')
    while sub_division[0] != '1' and sub_division[0] != '2':
        sub_division = input('Enter Subdivision: ')

    #scale validation
    while not scale_valid:
        scale = input('Enter Scale: ')
        scale = scale[0]
        if scale in 'abc':
            scale_valid = True
        else:
            scale_valid = False

    print('Enter employee classification:')

    #If structure to determine the pay_rate
    if division[0] == 'A':
        if sub_division[0] == '1':
            if scale[0] == 'a':
                pay_rate = 10.75
            elif scale[0] == 'b':
                pay_rate = 12.50
            elif scale[0] == 'c':
                pay_rate = 14.50

        elif sub_division[0] == '2':
            if scale[0] == 'a':
                pay_rate = 11.75
            elif scale[0] == 'b':
                pay_rate = 14.50
            elif scale[0] == 'c':
                pay_rate = 17.50

    if division[0] == 'B':
        if sub_division[0] == '1':
            if scale[0] == 'a':
                pay_rate = 13.00
            elif scale[0] == 'b':
                pay_rate = 16.00
            elif scale[0] == 'c':
                pay_rate = 18.50

        elif sub_division[0] == '2':
            if scale[0] == 'a':
                pay_rate = 15.00
            elif scale[0] == 'b':
                pay_rate = 18.50
            elif scale[0] == 'c':
                pay_rate = 22.00

    if division[0] == 'C':
        if sub_division[0] == '1':
            if scale[0] == 'a':
                pay_rate = 16.75
            elif scale[0] == 'b':
                pay_rate = 18.50
            elif scale[0] == 'c':
                pay_rate = 20.50

        elif sub_division[0] == '2':
            if scale[0] == 'a':
                pay_rate = 19.25
            elif scale[0] == 'b':
                pay_rate = 25.00
            elif scale[0] == 'c':
                pay_rate = 30.00

    #calculating the total pay depending on hours_worked
    if hours_worked <= 40:
        net_income = hours_worked * pay_rate
    else:
        net_income = (hours_worked + ((hours_worked - 40) * 1.5)) * pay_rate
    
    #Printing full_name, classification, and net_income
    print(f"Employee Name: {full_name}")
    print('Employee Classification: ', division, sub_division, scale, sep='')
    print('Total Pay:', format(net_income, ',.2f'))

    #asking for again/ another employee
    again = str(input("Do you want to enter another employee?")) ((hours_worked - 40) * 1.5)) * pay_rate

    #taking the frist element in the character list and capitalizing it
    again = again[0]
    again = again.upper()

    #decision to loop again or break
    if again in 'Y':
        continue
    else:
        break

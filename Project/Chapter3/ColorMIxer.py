#Asking for two primary colors
firstPrimary = str(input('Enter the first primary color.'))
secondPrimary = str(input('Enter the second primary color.'))

#IF structure and print
if(firstPrimary == 'yellow'):
    if(secondPrimary == 'blue'):
        print('The resulting color will be green.')
    elif(secondPrimary == 'red'):
        print('The resulting color will be orange.')
    else:
        print('Error! Run the program again!')  
elif(firstPrimary == 'red'):
    if(secondPrimary == 'yellow'):
        print('The resulting color will be orange.')
    elif(secondPrimary == 'blue'):
        print('The resulting color will be purple.')
    else:
        print('Error! Run the program again!')
elif(firstPrimary == 'blue'):
    if(secondPrimary == 'yellow'):
        print('The resulting color will be green.')
    elif(secondPrimary == 'red'):
        print('The resulting color will be purple.')
    else:
        print('Error! Run the program again!')
else:
    print('Error! Run the program again!')
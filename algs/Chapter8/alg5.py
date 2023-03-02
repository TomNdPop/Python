#definition function for the string acceptance 
def stringacceptance(mystring):
    if mystring.endswith('.com'):
        return True
    else:
        return False
    
def main():
    mystring = str(input('Enter a website: '))

    if stringacceptance(mystring) == True:
        print('You like business!')
    elif stringacceptance(mystring) ==False:
        print('You do not like business!')

main()
#Asking for the number of people attending
people_attend = float(input('How many people will be attending the cookout?'))

#Asking the user for the hotdogs per person
hdpp = float(input('How many hot dogs are in the package?'))
hdbpp = float(input('How many hot dog buns are in the package?'))
hpp = float(input('What is the number of hotdogs per person?'))

#calculating
total_hd = people_attend*hpp

#decision for package, minimium and then leftover
print()
if (total_hd % hdpp == 0):
    left_hd = total_hd % hdpp
    minimum_hd  = (total_hd // hdpp)
    print('The minimum amount of hot dog packages is: ',minimum_hd,'\n')
    print('The leftover amount of hot dogs is: ',left_hd,'\n')
else:
    if(total_hd % hdpp != 0):
        minimum_hd = (total_hd // hdpp) + 1
        left_hd = minimum_hd % hdpp
        print('The minimum amount of hot dog packages is: ',minimum_hd,'\n')
        print('The leftover amount of hot dogs is: ',left_hd,'\n')
        
if (total_hd % hdbpp == 0):
    minimum_hdb = (total_hd // hdbpp) 
    left_hdb = total_hd % hdbpp
    print('The minimum amount of hot dog bun packages is: ',minimum_hdb,'\n')
    print('The leftover amount of hot dog buns is: ',left_hdb,'\n')
else:
    if(total_hd % hdbpp != 0):
        minimum_hdb = (total_hd // hdbpp) + 1
        left_hdb = minimum_hdb % hdbpp
        print('The minimum amount of hot dog bun packages is: ',minimum_hdb,'\n')
        print('The leftover amount of hot dog buns is: ',left_hdb,'\n')  


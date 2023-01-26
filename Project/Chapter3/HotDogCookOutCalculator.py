#Asking for the number of people attending
people_attend = float(input('How many people will be attending the cookout?'))

#Asking the user for the hotdogs per person
hpp = float(input('What is the number of hotdogs per person?'))

#constants
hdpp = 10
hdbpp = 8

#calculating
total_hd = people_attend*hpp

minimum_hd  = (total_hd // hdpp) +()
minimum_hdb = (total_hd // hdbpp) + 1
left_hd = total_hd % hdpp
left_hdb = total_hd % hdbpp

#printing
print()
print('The minimum amount of hot dog packages is: ',minimum_hd,'\n')
print('The minimum amount of hot dog bun packages is: ',minimum_hdb,'\n')
print('The leftover amount of hot dogs is: ',left_hd,'\n')
print('The leftover amount of hot dog buns is: ',left_hdb,'\n')

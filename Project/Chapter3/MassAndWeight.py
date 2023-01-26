#Asking for the float of the mass
mass = float(input('Please enter the mass to convert to weight: '))

#calculating weight
weight  = 9.8 * mass

#if structure/ indication of the tolerance issues
if (weight < 100):
    print('This object is too light.')
elif(weight > 500):
    print('This object is too heavy. ')
else:
    print('Object is within acceptable limit.')
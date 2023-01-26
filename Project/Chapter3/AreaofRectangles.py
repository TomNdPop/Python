length1 = float(input('Length of the first is?'))
width1 = float(input('Width of the first is?'))
length2 = float(input('Length of the second is?'))
width2  = float(input('Width of the second is?'))

area1 = length1*width1
area2 = length2*width2

if area1 > area2:
    print('The first is larger than the second.')
else:
    if area2>area1:
        print('The second is larger than the first.')
    else: 
        print('They have the same area!')

#Asking for the pocket number
n = int(input('What is the number of the pocket?'))

#if structure to determine color
if(n==0):
    print('The pocket is green.')
elif(n==1):
    print('The pocket is red.')
elif n > 1 and n <= 10:
    if n%2 ==1:
        print('The pocket is red.')
    elif n%2 == 0:
        print('The pocket is black.')

elif n>=11 and n <=18:
    if n%2 ==1:
        print('The pocket is black.')
    elif n%2 == 0:
        print('The pocket is red.')
    
elif n>=19 and n <=28:
    if n%2 ==1:
        print('The pocket is red.')
    elif n%2 == 0:
        print('The pocket is black.')
  
elif n>=29 and n<=38:
    if n%2 ==1:
        print('The pocket is black.')
    elif n%2 == 0:
        print('The pocket is red.')
else:
    print('Wrong Number Moron.')


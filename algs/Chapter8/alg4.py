#Enter a string 
mystring = str(input('Input in a string to count the lowercase characters:'))

count = 0
#for loop to index into string
for ch in mystring:
    if ch.islower() == True:
        count += 1
    else:
        continue

#printing the count
print('The amount of lowercase characters in your string is:', count)

#Enter a string
user_string = str(input('Enter a string!'))
count = 0
space = ' '
#Use some type of loop
for space in user_string:
    if space == ' ':
        count += 1
    else:
        continue


#Print for count
print("The number of spaces is:", count)

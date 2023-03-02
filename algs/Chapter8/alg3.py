#Enter a string
user_string = str(input('Enter a string!'))
count = 0
space = ' '
#Use some type of loop
for space in user_string:
    if space in '1234567890':
        count += 1
    else:
        continue


#Print for count
print("The number of digit characters s:", count)

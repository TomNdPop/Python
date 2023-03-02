
User_name = str(input("Enter your first name: "))

with open('mytext.txt','a+') as outfile:
    outfile.write(User_name)
 
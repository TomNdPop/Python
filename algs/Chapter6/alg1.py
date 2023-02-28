output_file = open('my_name.txt', 'w')

#Asking the user for their name
User_name = str(input("Enter your first name:"))

output_file.write(User_name)
output_file.close()

# Initialize the variables
my_integer = 0
my_float = 0.00
my_string = ""



#integer validation
integer_valid = False
while not integer_valid:
    my_integer = int(input('Please provide an integer: '))
    if my_integer > 10:
        integer_valid = True
    else:
        print('Please input a valid integer! ')

#float Validation
float_valid = False
while not float_valid:
    my_float = float(input('Please provide a float: '))
    if my_float >= -1 and my_float <= 0:
        float_valid = True
    else:
        print('Please input a valid float! ')

#string validation
string_valid = False
while not string_valid:
    my_string = str(input('Please provide a vowel: '))
    my_string = my_string[0]
    if my_string in 'AEIOUaeiou':
        string_valid = True
    else:
        print('Please input a valid string!')


#Printing my_integer
print()
print(integer_valid)
print(f"My integer is :{my_integer}")
print()
#Printing my_float
print()
print(float_valid)
print(f"My integer is :{my_float}")
print()
#Printing my_string
print()
print(string_valid)
print(f"My integer is :{my_string}")
print()



#def that reverses string
def reversestring(mystring):
    new_string = ''
    for ch in mystring:
        new_string = ch + new_string
    return new_string
    

#def that takes user input
def main():
    mystring = str(input('Enter your sentence to reverse it!'))
    print(reversestring(mystring))

main()
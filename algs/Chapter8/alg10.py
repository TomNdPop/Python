def splice(mystring):
    new_string = mystring.split('>')
    return new_string


def main():
    mystring = str(input("Enter a new string!"))
    print(splice(mystring))


if __name__ == '__main__':
    main()
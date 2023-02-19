def my_function(a,b,c):
    a = b + c
    b = a + c
    c = a + b
    return a,b,c

def main():
    a,b,c = float(input('Enter in a number.'))
    print(my_function(a,b,c))

if __name__=='__main__':
    main()
    
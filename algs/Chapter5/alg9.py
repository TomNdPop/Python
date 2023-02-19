def timesTen(term):
    product = term *10
    return product

def main():
    term = float(input('Enter a number. '))
    print(timesTen(term))

if __name__=='__main__':
    main()
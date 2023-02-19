def cube(num):
    cube = num*num*num
    return cube

def main():
    num=input('Enter a number to return a cube: ')
    print(cube(num))

if __name__=='__main__':
    main()

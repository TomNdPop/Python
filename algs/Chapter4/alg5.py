
x = int(input('Enter a number: '))
sum = 0
for i in range(1,x+1):
    sum += i/(x+1-i)
print(sum)

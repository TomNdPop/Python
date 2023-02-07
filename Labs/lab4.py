

def isDivisibleBy(a,b):
  if a%b == 0:
    return True
  else:
    return False

def isPrime(number):
  divisor = 2
  while divisor < number:
    if isDivisibleBy(number, divisor) == True:
      return False
    elif isDivisibleBy(number, divisor + 1) == False:
      return True
    else: 
      divisor += 1

def isPrime(number):
  divisor = 2
  while divisor < number:
    if isDivisibleBy(number, divisor) == True:
      return False
    else: 
      divisor += 1
  return True  

def main():
  print("Result = ", isPrime(2))

main()

def main():
  num1 = ''
  num2 = ''

  try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1/num2

    if num1 <= 0 or num2 <= 0:
      raise ValueError

  except ValueError:
    print("You must enter valid numbers.")
  
  except ZeroDivisionError:
    print("You cannot divide by zero.")

  else:
    print("The division of", format(num1,",.1f"), "by", format(num2,",.1f"),"is", format(result,",.2f"),".")
  finally:
    print("Program Complete.")

if __name__ == '__main__':
  main()

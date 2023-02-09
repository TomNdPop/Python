speed = float(input("Enter a speed (mph): "))
hours = int(input("Enter the number of hours you have been traveling for: "))

for i in range(0,hours+1):
    total_miles = i * speed 
    print(total_miles)

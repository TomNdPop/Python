#calculating the cup per cookie per ingredient
sugarCup = 1.5/48
butterCup = 1/48
flourCup = 2.75/48

#Asking the user how many cookies they want to make
cookieCount = float(input('How many cookies do you want to make?'))

#calculating new cups per ingredient
sugarCup = sugarCup*cookieCount
butterCup = butterCup*cookieCount
flourCup = flourCup*cookieCount

#displaying the amounts in a field
print('The amount of sugar needed is', format(sugarCup, '12,.2f'))
print('The amount of butter needed is', format(butterCup, '11,.2f'))
print('The amount of flour needed is', format(flourCup, '12,.2f'))
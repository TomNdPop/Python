#Asking to input the celcius
cel = int(input('Input the current temperature to the nearest centigrade: '))
cel_cont = 9/5
 
# calculating the fahrenheit
fah = float(cel_cont*cel) + 32

#printing the float in a field rounded to the nearest tenths
print('or', format(fah, ',.2f'), ' fahrenheit')

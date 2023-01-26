#Asking for the date input
day = float(input('Enter a day in numeric form.'))
month = float(input('Enter a month in numeric form.'))
year = float(input('Enter a two digit year.'))

#calculating match year
match_year = day*month

#checking match year and the date input/ print statements
if(match_year==year):
    print('This is a magical year.')
else:
    print('This is not a magical year.')
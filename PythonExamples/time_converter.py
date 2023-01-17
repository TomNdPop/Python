#getting total number of seconds
total_seconds = int(input('How many total seconds are there?'))

#calculating total hours: 
hours = total_seconds // 3600

#calculating remaining minutes
minutes = (total_seconds // 60) % 60

# calculating the total remaining seconds
seconds = (total_seconds)%60

#printing the result
print('The total number of second: ',total_seconds)
print('Hours: ',hours)
print('Minutes: ',minutes)
print('Seconds: ', seconds)
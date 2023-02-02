cpm = float(input('How many calories do you burn per minute?'))
start_time = int(input('Now, input a starting time in minutes. '))
end_time = int(input('Now, input an ending time in minutes'))
gap_time = int(input('Now, input an interval time. (minutes)'))
total = 1
for time in range (start_time,end_time+gap_time,gap_time):
    total = time*cpm 
    print(total)
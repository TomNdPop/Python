#asking for current speed
speed = int(input("How fast are you currently driving (integers only)? "))

#Testing the speed if structure
if speed in range(24,56):
    print('Speed is normal.')
else:
    print('Speed is abnormal.')
total = 0
for i in [1,2,3,4,5]:
    if i == 1:
        number = int(input('How many bugs did you collect on your first day? '))
        total += number
    elif i == 2:
        number = int(input('How many bugs did you collect on your second day? '))
        total += number
    elif i == 3:
        number = int(input('How many bugs did you collect on your third day? '))
        total += number
    elif i == 4:
        number = int(input('How many bugs did you collect on your fourth day? '))
        total += number
    elif i == 5:
        number = int(input('How many bugs did you collect on your fifth day? '))
        total += number
print(f"You collected {total} bugs! Nice Work!")
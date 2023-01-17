#Score, 
Score = float(input('What was your score?'))

#Grade declarations
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 50 

#if structure
if Score >= A_score:
    print('Your grade is A.')
else:
    if Score >= B_score:
        print('Your grade is B.')
    else:
        if Score >= C_score:
            print('Your grade is C.')
        else: 
            if Score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
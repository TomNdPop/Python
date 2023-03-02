#open file
with open('number_list.txt','w+') as f:
#use a loop to write to the file
    for count in range(101):
        count = str(count)
        f.write(count + '\n')
    
#close the file

with open('number_list.txt','r') as f:
    print(f.read())
#function designed to turn all iterations of the character t in a string
#to a lowercase form and then copy the string
def t_translation(mystring):
    new_string = ''
    for ch in mystring:
        if ch == 't':
            new_string +=  ch.upper()
        else:
            new_string += ch
            continue
    return new_string

def main():
    mystring = str(input('What is the sentence?'))
    print(t_translation(mystring))

main()
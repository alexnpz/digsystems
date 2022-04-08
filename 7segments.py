# Define a dec funtion and then represent in 7 segments and print the format as well
# Input number to represent, if active 1 or 0, then calculate amount of 7 segments needed and how many segments are turn on
# Print the number with abcdefg format, print the number in accordance with 1/0 and print the representation as following (last to code)
"""
0 0 0 0 0 0 0     x x x x x x 1     2 2 2 2 2 2      
0 x x x x x 0     x x x x x x 1     x x x x x 2
0 x x x x x 0     x x x x x x 1     2 2 2 2 2 2
0 x x x x x 0     x x x x x x 1     2 x x x x x        ......    9
0 x x x x x 0     x x x x x x 1     2 x x x x x
0 x x x x x 0     x x x x x x 1     2 2 2 2 2 2
0 0 0 0 0 0 0     x x x x x x 1     
"""
# import random
# Define the amount of numbers to get the value in 7 segments
# Use random function to create these numbers and input the algorithm with these numbers
# Must use a pause when reaching end and/or comment the prints. Easier than this, could be write in a file the 7 segments format and the representation

dictletters = {   '0': 'a,b,c,d,e,f',
                  '1': 'b,c',
                  '2': 'a,b,d,e,g',
                  '3': 'a,b,c,d,g',
                  '4': 'b,c,f,g',
                  '5': 'a,c,d,f,g',
                  '6': 'a,c,d,e,f,g',
                  '7': 'a,b,c',
                  '8': 'a,b,c,d,e,f,g',
                  '9': 'a,b,c,f,g',
                  'A': 'a,b,c,e,f,g',
                  'B': 'c,d,e,f,g',
                  'C': 'a,d,e,f',
                  'D': 'b,c,d,e,g',
                  'E': 'a,d,e,f,g',
                  'F': 'a,e,f,g'}
dictletterposition = { 'a':0,
                       'b':1,
                       'c':2,
                       'd':3,
                       'e':4,
                       'f':5,
                       'g':6,}
numbposlist = list()
binoutputlist = list()
def sevensegms (hexword, act):
    output7seg = tuple(str(dictletters[hexword].replace(",","")))
    count_actives = len(output7seg)
    print('The number of segments turn on are :' + str(count_actives))
    print('The representation with the letters is : ' + str(dictletters [hexword]))
    for numbposition in output7seg:
        output7segnum = dictletterposition[numbposition]
        numbposlist.append(output7segnum)
    if act == '0':
        for segments in range(7):
            if segments in numbposlist:
                binoutputlist.append('0')
            else:
                binoutputlist.append('1')
    elif act == '1':
        for segments in range(7):
            if segments in numbposlist:
                binoutputlist.append('1')
            else:
                binoutputlist.append('0')
    else:
        print('Error')
    print('The binary representation is: ' + str(binoutputlist) + ' being active in ' + act)

while True:
    try:
        number_represent = int(input('Introduce the number to represent : '))
        number_represent_digits = len(str(number_represent))
        print('The amount of 7 segments required is :' + str(number_represent_digits))
        number_represent = list(str(number_represent))
        print(number_represent)
        act = input('Type 1 for active high and 0 for active low :')
        if act == '0' or act == '1':
            for values in number_represent:
                sevensegms(values,act)
        else:
            raise SystemExit('Must type 1 or 0 for the activation. Exiting program...')
    except:
         print('Integer error, Exiting Program...')
         break

    


# Implementation of a multiplexer

# While True, the input channels will be a list
# Separate the problem in 3: inputs formatting, funct mux and main
# If desirable, you can input the parameters as list/tuple :
# inputs = tuple(input(' Introduce number of inputs, number of selectors and selection value in that order(ex: 3,4,5) :' ))
# You could read the parameters from a file as well:
# import file as f
# filename = (input('Type the filename :')) + .'txt'
# with open (filename, encoding = 'utf-8) as f:
# Using a random function for creating inputs

import random
list_outputs = list()
print('Implementation of a MUX using a random generated input')

# Def Multiplexer
def mux(select,inputs):
    try:
       select = int(select)
       outputs = inputs[select]
       print('The value selected is :' + str(outputs))
       return outputs
    except:
        print('The number of selectors must be an integer')

# Escape function and validation of inputs
def validations (input):
    if input == 'q':
        raise SystemExit ('Exit Program')
    try:
        input = int(input)
    except:
        raise SystemExit ('The input parameters must be integer numbers, exiting program...')
    return int(input)

# Main Program
while True:
    selectors = input('Introduce the number of selectors for mux or type q to exit :')
    selectors = validations(selectors)
    if selectors <= 0:
        raise SystemExit ('The input value must be greater than 0')
    channels = 2**selectors
    print(' The number of channels is: ' + str(channels))
    value_selector = input('Introduce the selection value (starting from 0), up to ' + str(channels - 1) + ' or type q to exit :')
    value_selector = validations(value_selector)
    print(value_selector)
    if value_selector > 0 and value_selector <= channels - 1 :
        inputs = random.sample(range(1000),channels)
        print (inputs)
        list_outputs.append(mux(value_selector,inputs))
        print(' The values multiplexed in order are :' + str(list_outputs))
    else:
        raise SystemExit ('The input value must be from 0 up to ' + str(channels - 1))



# Implementation of a demultiplexer
# Use of a dictionary to keep old values and not replace them with every iteration
# Use of dict comprehension
import random
def validations (input):
    if input == 'q':
        raise SystemExit ('Exit Program')
    try:
        input = int(input)
    except:
        raise SystemExit ('The input parameters must be integer numbers, exiting program...')
    if input <= 0 :
        raise SystemExit('The selector must be greater than 0')
    return int(input)

inputs = random.randint(0,1000)
output_selector = input('Introduce the number of selectors :')
output_selector = validations(output_selector)
output_channels = 2**int(output_selector)
dictchannout = {i:[] for i in range(output_channels)}
print(dictchannout)

while True:
    channel_selected = input(f'Introduce the channel that will be the output (from 0 to {output_channels-1}) or q to exit the program: ')
    channel_selected = validations(channel_selected)
    if channel_selected > output_channels - 1 : 
        print ('Error, channel selected value must be lesser than the output value')
    else:
        dictchannout [channel_selected].append(inputs)
        print(dictchannout)
    inputs = random.randint(0,1000)
# Implementation of a demultiplexer
# Notice that if a channel selected with previous data saved is selected again, the data will be destroy. This can be improved by saving in a different way
import random

def validations (input):
    if input == 'q':
        raise SystemExit ('Exit Program')
    try:
        input = int(input)
    except:
        raise SystemExit ('The input parameters must be integer numbers, exiting program...')
    return int(input)

inputs = random.randint(0,1000)
output_selector = input('Introduce the number of selectors :')
output_selector = validations(output_selector)
if output_selector <= 0 :
    raise SystemExit('The selector must be greater than 0')
output_channels = 2**int(output_selector)
listchannout = [0 for i in range(output_channels)]

while True:
    channel_selected = input(f'Introduce the channel that will be the output (from 0 to {output_channels-1}) or q to exit the program: ')
    channel_selected = validations(channel_selected)
    listchannout.insert(channel_selected,inputs)
    print(listchannout)
    inputs = random.randint(0,1000)
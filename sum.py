# Raw implementation of sum, without carrying bits and inputs at digital gate
import random

sumt = 0b0
while True:
    try:
        number_inputs = int(input('Define the number of inputs :'))
        if type(number_inputs) is int:
            break
    except:
        print ('Number of inputs must be a natural number')
inputs = random.sample(range(100,999),int(number_inputs))
for value in inputs:
    sumt += value
print(format(sumt,'b'))
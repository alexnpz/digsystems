import random
# Implementation of not, according an input. This is, similar to bitwise operation
arrayinvert = list()
def invertgate(input):
    invertlist = list()
    input = format(input, 'b')
    print(f'The inverted values are {input}')
    for iter in input:
        if iter == '1':
            invertlist.append('0')
        else:
            invertlist.append('1')
    arrayinvert.append(invertlist)
    print(f'The array of inverted values is {invertlist}')
while True:
    try:
        number_inputs = int(input('Define the number of inputs :'))
        if type(number_inputs) is int:
            break
    except:
        print ('Number of inputs must be a natural number')
inputs = random.sample(range(100,999),int(number_inputs))
for value in inputs:
    print(f'The value of the input is {value}')
    invertgate(value)
print(f'The array of inverted values is {arrayinvert}')
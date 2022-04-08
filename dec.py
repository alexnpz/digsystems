# Implementation of decoder, given number of inputs and activation in 1 or 0
# Defining a decoder according its selection inputs and datafeed to activate the output
# Maybe, a dict could make this algorithm easier

def decoder(inputs,activation,ouputs):   
    list_representation = list()
    if activation == 0:
        for values in range(outputs):
            if values == inputs - 1:
                list_representation.insert(values,'0')
            else:
                list_representation.insert(values,'1')
        print(list_representation)
    elif activation == 1:
        for values in range(outputs):
            if values == inputs - 1:
                list_representation.insert(values,'1')
            else:
                list_representation.insert(values,'0')
        print(list_representation)
    else:
        print('Invalid program')
        return

def validations (input):
    if input == 'q':
        raise SystemExit('Exit Program')
    else:
        try:
            input = int(input)
        except:
            raise SystemExit ('The input parameters must be integer numbers, exiting program...')
        if input <= 0:
            raise SystemExit ('The input value must be greater than 0')
    return int(input)

while True:
        inputs = input('Type q to exit the program or Introduce the number for the decoder :')
        inputs = validations(inputs)
        numbsel = input('Type q to exit the program or Introduce the number of inputs for this decoder :')
        numbsel = validations(numbsel)
        activation = input('Introduce just 1 for active high in the outputs or 0 for active low in the outputs. Type q for exit :')
        activation = validations(activation)
        if activation != 1 and activation != 0:
            print('Invalid, the values should be only 0 or 1. Exiting program...')
            break
        outputs = 2**numbsel
        if inputs > outputs:
            raise SystemExit('Error, not possible that inputs should be greater thant outputs')
        dec = decoder(inputs,activation,outputs)
       
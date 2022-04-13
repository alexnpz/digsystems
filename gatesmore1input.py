# Implementation of generalized and, or, future -> nand, nor, xor and xand, for n inputs

from random import sample

# a = bin(28)
# b = bin(10))

# print(format(c,'b'))

while True:
    try:
        number_inputs = int(input('Define the number of inputs :'))
        if type(number_inputs) is int:
            break
    except:
        print ('Number of inputs must be a natural number')

inputs = sample(range(100,999),int(number_inputs))
print(inputs)
strwordlist = list()
lengthlist = list()
# If possible, use a dict for the values
# dictstrword = dict()

for iter in inputs:
    strword = bin(iter)[2:]
    strwordlist.append(strword)
    lengthlist.append(len(strword))

print(lengthlist)
#print(dictstrword)
mask_and = max(lengthlist) * '1'  
mask_or = max(lengthlist) * '0'
print(mask_and)
print(type(mask_and))
print(mask_or)

for iter in strwordlist:
    print(type(iter))
    mask_and = bin(int(mask_and,2) & int(iter,2))[2:]
    mask_or = bin(int(mask_or,2) | int(iter,2))[2:]
    print(mask_and)
    print(mask_or)
    
print(strwordlist)
# nor_gate = ~int(mask_or,2)
# nand_gate = ~int(mask_and,2)
print(f'Output and')
print(list(mask_and))
print(f'Output or')
print(list(mask_and))
# print(f'Output nand')
# print(list(nand_gate))
# print(f'Output nor')
# print(list(nor_gate))






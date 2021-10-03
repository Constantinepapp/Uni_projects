def dpa(input):
    stack = []
    alphabet = 'ST'

    for parenthesis in input:
        index = alphabet.index(parenthesis)
        if index == 0:
            stack.append('S')
        else:
            if len(stack) == 0:
                return "No"
            else:
                stack.pop()
    if len(stack) == 0:
        return "Yes"
    else:
        return "No"
     



inputs = ['TS','STTT','SSST','SSTSTSTTST','STST','SSTT','','S','ST','SST','SSTT','STT','STSTSSTT']

for input in inputs:
    boolean = dpa(input)
    print(input," : ",boolean)
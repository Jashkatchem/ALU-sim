def AND_gate(a,b):
    if a == 1 and b == 1:
        return 1
    else: 
        return 0
    
def XOR_gate(a,b):
    if a == 0:
        if b == 0:
            return 0
        else: 
            return 1
    else: 
        if b == 0:
            return 1
        else: 
            return 0
        
def OR_gate(a,b):
    if a == 1:
        return 1
    elif b == 1:
        return 1
    else: 
        return 0
    
def Half_Adder(a,b):
    #print(a)
    #print(b)
    sum = XOR_gate(a,b)
    carry = AND_gate(a,b)
    return sum, carry

def Full_Adder(a,b,c):
    sum1, carry1 = Half_Adder(a,b)
    sum2, carry2 = Half_Adder(sum1, c)
    carry3 = OR_gate(carry1, carry2)
    return sum2, carry3

def eight_bit_add(a,b):
    # we need to take the lists of digits and plug them into a half adder followed by a series of full adders in order to produce an output string. 
    result = []
    half_result = list(Half_Adder(int(a[7]), int(b[7])))
    sum = half_result[0]
    carry = half_result[1]
    #print(half_result)
    result.insert(0, sum)
    for n in range(1,8):
        sum, carry = Full_Adder(int(a[7-n]), int(b[7-n]), carry)
        result.insert(0, sum)
    # we need to check if there is still a carry and if so return an error. Otherwise, we need to concatenate result into a string and return it. 
    #if carry == 1: 
    #    return 00000000
    else:
        final = ''
        for val in result:
            final = final + str(val)
        return final
# we need to call eight_bit_add on two values read from a text and then write the result back to the text. Then we need to refactor the whole thing. 
file = open("Values.txt", "r")
value1 = file.readline()
value2 = file.readline()
file = open("Result.txt", "w")
file.write(eight_bit_add(value1, value2))

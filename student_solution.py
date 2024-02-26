# Convert hexadecimal to decimal
    # formula of converting hex to decimal
    #     1a= (1*16^(2-1) + 11*16^(2-2))
def hexToDecimal(hexString):
    hexString = hexString.upper() 
    for char in hexString:
        if char not in '0123456789ABCDEF':
            return "Invalid hexadecimal string"
        
    decimalValue = 0
    power = len(hexString) - 1
    index = 0
    
    while index < len(hexString):
        char = hexString[index]
        if char.isdigit():
            decimalValue += int(char)* (16**power)
        else:
            decimalValue += (ord(char) - ord('A') + 10) * (16**power)
        index+=1
        power-=1
    return decimalValue

# Convert decimal to binary
def decimalToBinary(decimalValue):
    binaryValue = ''
    if decimalValue==0:
        return 0
    while decimalValue >0:
        remainder = decimalValue % 2
        binaryValue = str(remainder) + binaryValue
        decimalValue //=2
    return binaryValue
    

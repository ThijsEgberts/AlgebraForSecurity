import ctypes

class BigNumber:
    
    exponents = [] #a list of exponents for the exponential representation of the number, so 3 in binary will be represented as [1,1]
    radix = None
    sign = 1 #1 = positive, 0 = negative
    
    #Construct a BigNumber from a radix, list of exponents and the sign of the number
    def __init__(self, radix, exponents, sign) -> None:
        self.radix = radix
        self.exponents = exponents
        self.sign = sign
    
    #Construct a BigNumber from a string
    def __init__(self, string, radix) -> None:
        self.parseString(string, radix)
    
    #Parses a string representing a number to a BigNumber format
    def parseString(stringNr, radix):
        return None
    
    
    
from fixedint import Int32, MutableInt32
import string

class BigNumber:
    
    exponents = [] #a list of exponents for the exponential representation of the number, so 3 in binary will be represented as [1,1]
    radix = Int32(0)
    isNegative = 0
    
    #Construct a BigNumber from a radix, list of exponents and the sign of the number
    def __init__(self, radix : Int32, exponents : [Int32], isNegative : int) -> None:
        self.radix = Int32(radix)
        self.exponents = exponents
        self.isNegative = isNegative #isNegative as a 1 or 0 boolean representation
    
    #Construct a BigNumber from a string
    def __init__(self, string : string, radix : Int32) -> None:
        self.radix = Int32(radix)
        self.parseString(string, radix)
    
    #Parses a string representing a number to a BigNumber format
    def parseString(self, stringNr : string, radix : Int32):
        self.exponents = [None] * len(stringNr) #create a list of exponents with the length of the string

        if radix <= 0 or radix > 16: #check correct format
            self.radix = Int32(radix)
        
        #check if the number is negative
        if stringNr[0] == "-":
            self.isNegative = 1
        else:
            self.isNegative = 0
        
        #parse each digit in the string and convert it to a number in the exponent list
        for i in range(self.isNegative, len(stringNr)): #skip the minus sign if the number is negative
            match stringNr[i]:
                case '0':
                    self.exponents[i] = Int32(0)
                case '1':
                    self.exponents[i] = Int32(1)
                case '2':
                    self.exponents[i] = Int32(2)
                case '3':
                    self.exponents[i] = Int32(3)
                case '4':
                    self.exponents[i] = Int32(4)
                case '5':
                    self.exponents[i] = Int32(5)
                case '6':
                    self.exponents[i] = Int32(6)
                case '7':
                    self.exponents[i] = Int32(7)
                case '8':
                    self.exponents[i] = Int32(8)
                case '9':
                    self.exponents[i] = Int32(9)
                case 'A':
                    self.exponents[i] = Int32(10)
                case 'B':
                    self.exponents[i] = Int32(11)
                case 'C':
                    self.exponents[i] = Int32(12)
                case 'D':
                    self.exponents[i] = Int32(13)
                case 'E':
                    self.exponents[i] = Int32(14)
                case 'F':
                    self.exponents[i] = Int32(15)
                case _ :
                    raise Exception('Radix out of bounds')

    def __str__(self):
        return "Radix: " + str(self.radix) + " Exponents: " + str(self.exponents) + " isNegative: " + str(self.isNegative)                

def matchExponentsLength(x : BigNumber, y : BigNumber):
        """
        Matches the length of the exponents of two BigNumbers by adding 0's to the front of the list.
        """
        if len(x.exponents) > len(y.exponents):
            for i in range(len(x.exponents) - len(y.exponents)):
                y.exponents.insert(0, Int32(0))
        elif len(x.exponents) < len(y.exponents):
            for i in range(len(y.exponents) - len(x.exponents)):
                x.exponents.insert(0, Int32(0))

from fixedint import Int32, MutableInt32
import string


class BigNumber:

    exponents = []  # a list of exponents for the exponential representation of the number, so 3 in binary will be represented as [1,1]
    radix = Int32(0)
    isNegative = 0

    # Construct a BigNumber from a string
    # def __init__(self, string: string, radix: Int32) -> None:
    #     self.radix = Int32(radix)
    #     self.parseString(string, radix)
    def __init__(self, radix: Int32, exponents: [Int32], isNegative: int) -> None:
        self.radix = Int32(radix)
        self.exponents = exponents
        self.isNegative = isNegative

    #python hacky way of making multiple constructors
    @classmethod
    def createNumberFromString(cls, stringNr: string, radix: Int32):
        exponentList, sign = cls.parseString(stringNr, radix)
        return cls(radix, exponentList, sign)
    
    @classmethod
    def createZero(cls, radix : Int32):
        return cls(radix, [Int32(0)], 0)
    
    @classmethod
    def createOne(cls, radix : Int32):
        return cls(radix, [Int32(1)], 0)
    
    def parseString(stringNr, radix):
        if (stringNr == ""):
            raise Exception('Empty string')

        if radix <= 0 or radix > 16:  # check correct format
            raise Exception('radix out of bounds')

        # check if the number is negative
        if stringNr[0] == "-":
            isNegative_ = 1
            stringNr = stringNr[1:]
        else:
            isNegative_ = 0

        length = len(stringNr)

        # create a list of exponents with the length of the string
        exponents_ = [None] * length

        # parse each digit in the string and convert it to a number in the exponent list
        for i in range(length):
            match stringNr[i]:
                case '0':
                    exponents_[i] = Int32(0)
                case '1':
                    exponents_[i] = Int32(1)
                case '2':
                    exponents_[i] = Int32(2)
                case '3':
                    exponents_[i] = Int32(3)
                case '4':
                    exponents_[i] = Int32(4)
                case '5':
                    exponents_[i] = Int32(5)
                case '6':
                    exponents_[i] = Int32(6)
                case '7':
                    exponents_[i] = Int32(7)
                case '8':
                    exponents_[i] = Int32(8)
                case '9':
                    exponents_[i] = Int32(9)
                case 'A':
                    exponents_[i] = Int32(10)
                case 'B':
                    exponents_[i] = Int32(11)
                case 'C':
                    exponents_[i] = Int32(12)
                case 'D':
                    exponents_[i] = Int32(13)
                case 'E':
                    exponents_[i] = Int32(14)
                case 'F':
                    exponents_[i] = Int32(15)
        return exponents_, isNegative_
    
    # # Parses a string representing a number to a BigNumber format
    # def parseString_(self, stringNr: string, radix: Int32):

    #     if (stringNr == ""):
    #         raise Exception('Empty string')

    #     if radix > 0 and radix <= 16:  # check correct format
    #         self.radix = Int32(radix)

    #     # check if the number is negative
    #     if stringNr[0] == "-":
    #         self.isNegative = 1
    #         stringNr = stringNr[1:]
    #     else:
    #         self.isNegative = 0

    #     length = len(stringNr)

    #     # create a list of exponents with the length of the string
    #     self.exponents = [None] * length

    #     # parse each digit in the string and convert it to a number in the exponent list
    #     for i in range(0, length):  # skip the minus sign if the number is negative
    #         match stringNr[i]:
    #             case '0':
    #                 self.exponents[i] = Int32(0)
    #             case '1':
    #                 self.exponents[i] = Int32(1)
    #             case '2':
    #                 self.exponents[i] = Int32(2)
    #             case '3':
    #                 self.exponents[i] = Int32(3)
    #             case '4':
    #                 self.exponents[i] = Int32(4)
    #             case '5':
    #                 self.exponents[i] = Int32(5)
    #             case '6':
    #                 self.exponents[i] = Int32(6)
    #             case '7':
    #                 self.exponents[i] = Int32(7)
    #             case '8':
    #                 self.exponents[i] = Int32(8)
    #             case '9':
    #                 self.exponents[i] = Int32(9)
    #             case 'A':
    #                 self.exponents[i] = Int32(10)
    #             case 'B':
    #                 self.exponents[i] = Int32(11)
    #             case 'C':
    #                 self.exponents[i] = Int32(12)
    #             case 'D':
    #                 self.exponents[i] = Int32(13)
    #             case 'E':
    #                 self.exponents[i] = Int32(14)
    #             case 'F':
    #                 self.exponents[i] = Int32(15)
    #             case _:
    #                 raise Exception('Radix out of bounds')

    def __str__(self):
        # return "[" + self.exponentsToString() + "]_" + str(self.radix)
        return self.exponentsToString()

    # flips the sign of the big number, ei -1 becomes 1
    def flipSign(self):
        if bool(self.isNegative):
            self.isNegative = 0
            return self
        else:
            self.isNegative = 1
            return self

    def setSign(self, sign: int):
        self.isNegative = sign
        return self

    def removeLeadingZeroes(self):
        removeUntil = 0

        for i in range(0, len(self.exponents) - 1):
            if self.exponents[i] == 0:
                removeUntil += 1
            else:
                break

        for i in range(0, removeUntil):
            del self.exponents[0]

    def exponentsToString(self):
        self.removeLeadingZeroes()
        output = ""
        if (self.isNegative):
            output = "-"
        for exponent in self.exponents:
            if (exponent >= 10):
                output += string.ascii_uppercase[exponent - 10]
            else:
                output += str(exponent)

        return output
    
    def isZero(self) -> bool:
        if len(self.exponents) == 1 and self.exponents[0] == Int32(0):
            return True
        else:
            for i in range(len(self.exponents)): #in case of leading or trailing zeroes
                if self.exponents[i] != Int32(0):
                    return False
            return True
        
    def compare(self, other: 'BigNumber', greater_or_equal: bool = False) -> bool:
        """
        Compares this BigNumber to another BigNumber.

        Args:
            other (BigNumber): The BigNumber to compare with.
            greater_or_equal (bool): If True, performs a greater than or equal to comparison.
                                        If False, performs a greater than comparison.

        Returns:
            bool: True if the comparison condition is met, False otherwise.
        """
        if self.isNegative != other.isNegative:
            return other.isNegative

        #if a number has strictly more exponents its bigger
        if len(self.exponents) > len(other.exponents):
            return True
        elif len(self.exponents) < len(other.exponents):
            return False

        # Compare the exponents from left to right
        for i in range(len(self.exponents)):
            if self.exponents[i] > other.exponents[i]:
                return True
            elif self.exponents[i] < other.exponents[i]:
                return False

        return True if greater_or_equal else False

    def matchExponentsLength(self, other: 'BigNumber'):
        """
        Matches the length of the exponents of this BigNumber and another BigNumber
        by adding 0's to the front of the list.
        """
        if len(self.exponents) > len(other.exponents):
            for i in range(len(self.exponents) - len(other.exponents)):
                other.addLeadingZero()
        elif len(self.exponents) < len(other.exponents):
            for i in range(len(other.exponents) - len(self.exponents)):
                self.addLeadingZero()

    def addLeadingZero(self):
        self.exponents.insert(0, Int32(0))

    # Only works with positive shift
    def bitShift(self, shift: int):
        # x = createBigNumberFromExponents(
        #     self.radix, self.exponents, self.isNegative)
        x = BigNumber(self.radix, self.exponents, self.isNegative)
        for _ in range(shift):
            x.exponents.append(0)
        return x


# def createBigNumberFromExponents(radix, exponents, isNegative):
#     x = BigNumber("0", radix)
#     x.exponents = exponents.copy()
#     x.isNegative = isNegative
#     return x
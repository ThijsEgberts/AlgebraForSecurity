from fixedint import Int32, MutableInt32
import string


class BigNumber:

    exponents = []  # a list of exponents for the exponential representation of the number, so 3 in binary will be represented as [1,1]
    radix = Int32(0)
    isNegative = 0

    # Construct a BigNumber from a string
    def __init__(self, string: string, radix: Int32) -> None:
        self.radix = Int32(radix)
        self.parseString(string, radix)

    # Parses a string representing a number to a BigNumber format
    def parseString(self, stringNr: string, radix: Int32):

        if (stringNr == ""):
            raise Exception('Empty string')

        if radix <= 0 or radix > 16:  # check correct format
            self.radix = Int32(radix)

        # check if the number is negative
        if stringNr[0] == "-":
            self.isNegative = 1
            stringNr = stringNr[1:]
        else:
            self.isNegative = 0

        length = len(stringNr)

        self.exponents = [None] * length #create a list of exponents with the length of the string
        
        #parse each digit in the string and convert it to a number in the exponent list
        for i in range(0, length): #skip the minus sign if the number is negative
            match stringNr[i + self.isNegative]:
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
                case _:
                    raise Exception('Radix out of bounds')

    def __str__(self):
        #return "[" + self.exponentsToString() + "]_" + str(self.radix)
        return self.exponentsToString()

    # flips the sign of the big number, ei -1 becomes 1
    def flipSign(self):
        if bool(self.isNegative):
            self.isNegative = 0
            return self
        else:
            self.isNegative = 1
            return self

    def setSign(self, sign: bool):
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

# TODO Dit kan sws wel iets compacter, letterlijk 2x dezelfde code :skull:


def isGreaterThan(x: BigNumber, y: BigNumber):
    """
    Checks if x is greater than y.

    The algorithm is as follows:
    1. Check if the signs are different
    2. If the signs are different, return true if x is positive and y is negative, else return false
    3. If the signs are the same, check the length of the exponents
    4. If the length of the exponents is different, return true if x is longer than y, else return false
    5. If the length of the exponents is the same, check the exponents from left to right
    6. Return true if x is greater than y, else return false
    """

    # 1. Check if the signs are different
    if x.isNegative != y.isNegative:
        # 2. If the signs are different, return true if x is positive and y is negative, else return false
        if x.isNegative == 0:
            return True
        else:
            return False

    # 3. If the signs are the same, check the length of the exponents
    if len(x.exponents) > len(y.exponents):
        # 4. If the length of the exponents is different, return true if x is longer than y, else return false
        return True
    elif len(x.exponents) < len(y.exponents):
        return False
    else:
        # 5. If the length of the exponents is the same, check the exponents from left to right
        for i in range(len(x.exponents)):
            # 6. Return true if x is greater than y, else return false
            if x.exponents[i] > y.exponents[i]:
                return True
            elif x.exponents[i] < y.exponents[i]:
                return False
    return False


def isGreaterOrEqual(x: BigNumber, y: BigNumber):
    """
    Checks if x is greater or equal to y.

    The algorithm is as follows:
    1. Check if the signs are different
    2. If the signs are different, return true if x is positive and y is negative, else return false
    3. If the signs are the same, check the length of the exponents
    4. If the length of the exponents is different, return true if x is longer than y, else return false
    5. If the length of the exponents is the same, check the exponents from left to right
    6. Return true if x is greater than y, return false if y is greater than x, else return true
    """

    # 1. Check if the signs are different
    if x.isNegative != y.isNegative:
        # 2. If the signs are different, return true if x is positive and y is negative, else return false
        if x.isNegative == 0:
            return True
        else:
            return False

    # 3. If the signs are the same, check the length of the exponents
    if len(x.exponents) > len(y.exponents):
        # 4. If the length of the exponents is different, return true if x is longer than y, else return false
        return True
    elif len(x.exponents) < len(y.exponents):
        return False
    else:
        # 5. If the length of the exponents is the same, check the exponents from left to right
        for i in range(len(x.exponents)):
            # 6. Return true if x is greater than y, else return false
            if x.exponents[i] > y.exponents[i]:
                return True
            elif x.exponents[i] < y.exponents[i]:
                return False
    return True


def matchExponentsLength(x: BigNumber, y: BigNumber):
    """
    Matches the length of the exponents of two BigNumbers by adding 0's to the front of the list.
    """
    if len(x.exponents) > len(y.exponents):
        for i in range(len(x.exponents) - len(y.exponents)):
            addLeadingZero(y)
    elif len(x.exponents) < len(y.exponents):
        for i in range(len(y.exponents) - len(x.exponents)):
            addLeadingZero(x)


def addLeadingZero(x: BigNumber):
    x.exponents.insert(0, Int32(0))


def copyBigNumber(x: BigNumber):
    return createBigNumberFromExponents(x.radix, x.exponents, x.isNegative)

# Only works with positive shift


def bitShift(original: BigNumber, shift: int):
    x = copyBigNumber(original)
    for _ in range(shift):
        x.exponents.append(0)
    return x


def createBigNumberFromExponents(radix, exponents, isNegative):
    x = BigNumber("0", radix)
    x.exponents = exponents.copy()
    x.isNegative = isNegative
    return x

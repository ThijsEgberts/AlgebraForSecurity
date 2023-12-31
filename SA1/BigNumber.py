import string


class BigNumber:

    exponents = []  # a list of exponents for the exponential representation of the number, so 3 in binary will be represented as [1,1]
    radix = 0
    isNegative = False

    # Construct a BigNumber from an exponents list
    def __init__(self, radix: int, exponents: list, isNegative: bool) -> None:
        self.radix = radix
        self.exponents = exponents
        self.isNegative = bool(isNegative)

    # Parses a string representing a number to a BigNumber format
    def parseString(self, stringNr: string, radix: int):

        if (stringNr == ""):
            raise Exception('Empty string')

        if radix <= 0 or radix > 16:  # check correct format
            self.radix = radix

        # check if the number is negative
        if stringNr[0] == "-":
            self.isNegative = True
            stringNr = stringNr[1:]
        else:
            self.isNegative = False

        length = len(stringNr)

        # create a list of exponents with the length of the string
        self.exponents = [None] * length

        # parse each digit in the string and convert it to a number in the exponent list
        for i in range(0, length):
            match stringNr[i]:
                case '0':
                    self.exponents[i] = 0
                case '1':
                    self.exponents[i] = 1
                case '2':
                    self.exponents[i] = 2
                case '3':
                    self.exponents[i] = 3
                case '4':
                    self.exponents[i] = 4
                case '5':
                    self.exponents[i] = 5
                case '6':
                    self.exponents[i] = 6
                case '7':
                    self.exponents[i] = 7
                case '8':
                    self.exponents[i] = 8
                case '9':
                    self.exponents[i] = 9
                case 'A':
                    self.exponents[i] = 10
                case 'B':
                    self.exponents[i] = 11
                case 'C':
                    self.exponents[i] = 12
                case 'D':
                    self.exponents[i] = 13
                case 'E':
                    self.exponents[i] = 14
                case 'F':
                    self.exponents[i] = 15
                case _:
                    raise Exception('Radix out of bounds')

    def __str__(self):
        return self.exponentsToString()

    # flips the sign of the big number, ei -1 becomes 1
    def flipSign(self):
        if bool(self.isNegative):
            self.isNegative = False
            return self
        else:
            self.isNegative = True
            return self

    def setSign(self, sign: bool):
        self.isNegative = bool(sign)
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

    #prints out the exponent list as a string, e.i. the base radix representation of the number
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
        if len(self.exponents) == 1 and self.exponents[0] == 0:
            return True

        return all(exponent == 0 for exponent in self.exponents)

    def isOne(self) -> bool:
        if len(self.exponents) == 1 and self.exponents[0] == 1:
            return True

        return all(exponent == 0 for i, exponent in enumerate(self.exponents) if i != len(self.exponents) - 1) and self.exponents[-1] == 1

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

        # Match the length of the exponents
        self.matchExponentsLength(other)

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
        len_diff = len(self.exponents) - len(other.exponents)
        if len_diff > 0:
            other.exponents = [0] * len_diff + other.exponents
        elif len_diff < 0:
            self.exponents = [0] * abs(len_diff) + self.exponents

    def addLeadingZero(self):
        self.exponents.insert(0, 0)

    # Shifts number x digits left, adding 0
    def shiftLeft(self, shift: int):
        x = BigNumber(
            self.radix, self.exponents.copy(), self.isNegative)
        for _ in range(shift):
            x.exponents.append(0)
        return x
    
    def toInt(self):
        return int(self.exponentsToString(), self.radix)


def createBigNumberFromString(string: str, radix: int):
    bn = BigNumber(radix, [], 0)
    bn.parseString(string, radix)
    return bn
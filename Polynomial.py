import string


class Polynomial:

    coefficients = []  # a list of coefficients for the representation of the polynomial
    radix = 0

    # Construct a Polynomial from an coefficients list
    def __init__(self, radix: int, coefficients: list) -> None:
        self.radix = radix
        self.coefficients = coefficients

    # Parses a string representing a coefficients to a Polynomial format
    def parseString(self, stringNr: string, radix: int):
        """
        Parses a string representing a coefficients to a Polynomial format. Coefficients are split by spaces. 
        String starts with the lowest degree coefficient and ends with the highest degree coefficient.

        Args:
            stringNr (string): The string to parse.
            radix (int): The radix of the coefficients.

        Raises: 
            Exception: If the string is empty.
            Exception: If the radix is out of bounds.
            Exception: If the string contains an invalid character. 
            Exception: If the coefficients contain an invalid coefficient.
            Exception: If the last coefficient is zero.       
        """

        if (stringNr == ""):
            raise Exception('Empty string')

        if not (509 >= radix and radix >= 2):  # check correct format
            raise Exception('Radix out of bounds')

        if not all(char in string.printable for char in stringNr):
            raise Exception('Invalid character')

        self.radix = radix

        # split the string into a list of coefficients
        stringNr = stringNr.split(' ')
        length = len(stringNr)

        # create a list of integers with the length of the string
        self.coefficients = [None] * length

        # parse each digit in the string and convert it to a number in the coefficient list
        for i in range(0, length):
            self.coefficients[i] = int(stringNr[i])

        # create a list of coefficients with the length of the string
        self.coefficients = [None] * length

        # parse each digit in the string and convert it to a number in the coefficient list
        for i in range(0, length):
            self.coefficients[i] = int(stringNr[i])

        # Check if each integer is between 0 and radix - 1 (ignoring negative sign)
        if not all(0 <= abs(coefficient) < radix for coefficient in self.coefficients):
            raise Exception('Invalid coefficient')

        # Check if last coefficient is non-zero
        if self.coefficients[-1] == 0:
            raise Exception('Last coefficient is zero')

    # TODO fix every function below this line

    def __str__(self):
        return self.coefficientsToString()

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

        for i in range(0, len(self.coefficients) - 1):
            if self.coefficients[i] == 0:
                removeUntil += 1
            else:
                break

        for i in range(0, removeUntil):
            del self.coefficients[0]

    def isZero(self) -> bool:
        if len(self.coefficients) == 1 and self.coefficients[0] == 0:
            return True

        return all(coefficient == 0 for coefficient in self.coefficients)

    def isOne(self) -> bool:
        if len(self.coefficients) == 1 and self.coefficients[0] == 1:
            return True

        return all(coefficient == 0 for i, coefficient in enumerate(self.coefficients) if i != len(self.coefficients) - 1) and self.coefficients[-1] == 1

    def compare(self, other: 'Polynomial', greater_or_equal: bool = False) -> bool:
        """
        Compares this Polynomial to another Polynomial.

        Args:
            other (Polynomial): The Polynomial to compare with.
            greater_or_equal (bool): If True, performs a greater than or equal to comparison.
                                        If False, performs a greater than comparison.

        Returns:
            bool: True if the comparison condition is met, False otherwise.
        """
        if self.isNegative != other.isNegative:
            return other.isNegative

        # Match the length of the coefficients
        self.matchcoefficientsLength(other)

        # Compare the coefficients from left to right
        for i in range(len(self.coefficients)):
            if self.coefficients[i] > other.coefficients[i]:
                return True
            elif self.coefficients[i] < other.coefficients[i]:
                return False

        return True if greater_or_equal else False

    def matchcoefficientsLength(self, other: 'Polynomial'):
        """
        Matches the length of the coefficients of this Polynomial and another Polynomial
        by adding 0's to the front of the list.
        """
        len_diff = len(self.coefficients) - len(other.coefficients)
        if len_diff > 0:
            other.coefficients = [0] * len_diff + other.coefficients
        elif len_diff < 0:
            self.coefficients = [0] * abs(len_diff) + self.coefficients

    def addLeadingZero(self):
        self.coefficients.insert(0, 0)

    # Shifts number x digits left, adding 0
    def shiftLeft(self, shift: int):
        x = Polynomial(
            self.radix, self.coefficients.copy(), self.isNegative)
        for _ in range(shift):
            x.coefficients.append(0)
        return x


def createPolynomialFromString(string: str, radix: int):
    poly = Polynomial(radix, [], 0)
    poly.parseString(string, radix)
    return poly

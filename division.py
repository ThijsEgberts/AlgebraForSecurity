from BigNumber import BigNumber
from addition_subtraction import solve_addition_integer_arithmetic, solve_subtraction_integer_arithmetic
from multiplication_karatsuba import solve_multiplication_karatsuba
from BigNumber import createBigNumberFromString

def solve_division_with_remainder(x: BigNumber, y: BigNumber) -> list[BigNumber]:

    return long_division_with_remainder(x, y)

def long_division_with_remainder(x: BigNumber, y: BigNumber) -> list[BigNumber]:

    #Letters and structure based on lecture notes Algorithm 1.6

    m = len(x.exponents)
    n = len(y.exponents)

    #1.1
    r = BigNumber(x.radix, x.exponents, x.isNegative)

    #1.2
    k = m - n + 1

    #Init array
    q = BigNumber(x.radix, [0] * k, 0)

    #2.1
    for i in range(k-1, -1, -1):
        #2.2
        q.exponents[k - i - 1] = division_by_subtraction_with_remainder(r, y.shiftLeft(i))[0].exponents[0]
        #2.3
        r = solve_subtraction_integer_arithmetic(r, solve_multiplication_karatsuba(BigNumber(10, [q.exponents[k - i - 1]], 0), y).shiftLeft(i))

    q.removeLeadingZeroes()

    return q, r

def division_by_subtraction_with_remainder(x_: BigNumber, y_: BigNumber) -> list[BigNumber]:
    """
    Solves the division with remainder of two numbers.
    Returns the quotient and the remainder in form [quotient, remainder]

    The algorithm is as follows:
    1. While x is greater or equal to y, subtract y from x.
    2. Add 1 to the quotient.
    3. Return the quotient and the remainder.

    This is based on Euclid's algorithm.
    """
    x = BigNumber(x_.radix, x_.exponents.copy(), x_.isNegative)
    y = BigNumber(y_.radix, y_.exponents.copy(), y_.isNegative)

    quotient = BigNumber(x.radix, [0], 0)
    one = BigNumber(x.radix, [1], 0)

    while x.compare(y, greater_or_equal=True):
        # Calculate the remainder after subtracting y from x
        x = solve_subtraction_integer_arithmetic(x, y)
        # Add 1 to the quotient
        quotient = solve_addition_integer_arithmetic(quotient, one)

    # Result contains the quotient and the remainder in form [quotient, remainder]
    return [quotient, x]

x = createBigNumberFromString("23167A2509445A678A51A9192373268972293283A5108274A590525003083814962AA9014419161722789124329020880124383A097818A18729097069879715AA7711787015336787A30808237038788704896463259286A8AA489818804547691A524A7254975A53160773232751A53481177A4875640272412418485515198693153408124562346804622555909770731822AA7A331A511A9882A1359642901A0330073A820837164816105961993703AA76A80841680574470882272A6443791153676341232851285A956578988679943210475514756735A436A6465795507190026252275940A53870762782", 11)
y = createBigNumberFromString("A50681346896A86133779511A12453A7421967915109241298A3AA25558899584035880500A06604598373400685734389931236582717738A7479178479219A141808555037623655A710394210584671668A57589A596882154296433834A59878969432944546970576771129A6832043A172009869A071952959839335437172227A696446835AAA4A995216590933A853409A8A07A2AA8235A3824371787787157380828470398673A988272419A857A4174138374098699722008A77303A2A476A03766270A9100964756A49A6641982349558581A8403783867627579A51832711142A980937A6341", 11)
(q, r) = long_division_with_remainder(x, y)
(q, r) = division_by_subtraction_with_remainder(x, y)
def rect(area, perimeter):

    """Return the longest side of a rectangle with AREA and PERIMETER that has integer sides.
    >>> rect(10, 14) # A 2 x 5 rectangle
    5
    >>> rect(5, 12) # A 1 x 5 rectangle
    5
    >>> rect(25, 20) # A 5 x 5 rectangle
    5
    >>> rect(25, 25) # A 2.5 x 10 rectangle doesn't count because sides are not integers
    False
    >>> rect(25, 29) # A 2 x 12.5 rectangle doesn't count because sides are not integers
    False
    >>> rect(100, 50) # A 5 x 20 rectangle
    20
    >>> rect(5, 11)
    False
    >>> rect(4, 11)
    False
    """
    # uses quadratic formula
    discriminant = (0.5 * perimeter) ** 2 - 4 * area

    side_1 = (0.5 * perimeter + discriminant ** 0.5) / 2
    side_2 = area / side_1

    if side_1 != int(side_1) or side_2 != int(side_2):
        return False
    
    return max(int(side_1), int(side_2))

    
def sequence(n, term):

    """Return the first n terms of a sequence as an integer.
    >>> sequence(6, abs) # Terms are 1, 2, 3, 4, 5, 6
    123456
    >>> sequence(5, lambda k: k+8) # Terms are 9, 10, 11, 12, 13
    910111213
    >>> sequence(4, lambda k: pow(10, k)) # Terms are 10, 100, 1000, 10000
    10100100010000
    """
    concat_int = 0
    for i in range(1, n+1):
        coeff = 1
        val = term(i)
        while coeff <= val:
            coeff *= 10
        concat_int = concat_int * coeff + val
    return concat_int



def repeat(k):

    """When called repeatedly, print each repeated argument.
    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(lambda n: False)(k)

def detector(f):
    def g(i):
        if f(i):
            print(i)
        return detector(lambda n: n == i or f(n))
    return g



def repeat_digits(n):

    """Print the repeated digits of non-negative integer n.
    >>> repeat_digits(581002821)
    2
    0
    1
    8
    """
    f = repeat
    while n > 0:
        digit = n % 10
        f = f(digit)
        n //= 10
        
def same_digits(a, b):
    """
    Implement same_digits, which takes two positive integers. It returns whether they both become
    the same number after replacing each sequence of a digit repeated consecutively with only one of that
    digit. For example, in 12222321, the sequence 2222 would be replaced by only 2, leaving 12321.
    Restriction: You may only write combinations of the following in the blanks:
    a, b, end, 10, %, if, while, and, or, ==, !=, True, False, and return. (No division allowed!)

    >>> same_digits(2002200, 2202000) # Ignoring repeats, both are 2020
    True
    >>> same_digits(21, 12) # Digits must appear in the same order
    False
    >>> same_digits(12, 2212) # 12 and 212 are not the same
    False
    >>> same_digits(2020, 20) # 2020 and 20 are not the same
    False
    """
    assert a > 0 and b > 0
    while a and b:
        if a != b:
            end = a % 10
            while end == a % 10:
                a = a // 10
            while end == b % 10:
                b = b // 10
        else:
            return True
    return a == b

# ORIGINAL SKELETON FOLLOWS

# def same_digits(a, b):
#     assert a > 0 and b > 0
#     while a and b:
#         if ______:
#             end = a % 10
#             while ______:
#                 a = a // 10
#             while ______:
#                 b = b // 10
#         else:
#             ______
#     ______


def no_repeats(a):

    """Remove repeated adjacent digits from a.
    >>> no_repeats(22000200)
    2020
    """
    return search(lambda x: same_digits(x, a), 1)

def search(f, x):

    while not f(x):
        x += 1
    return x


def unique_largest(n):

    """Return whether the largest digit in n appears only once.
    >>> unique_largest(132123) # 3 is largest and appears twice
    False
    >>> unique_largest(1321523) # 5 is largest and appears only once
    True
    >>> unique_largest(5)
    True
    """
    assert n > 0
    top = 0
    while n:
        n, d = n // 10, n % 10
        if d > top:
            top, unique = d, True
        elif d == top:
            unique = False
    return unique

# Skeleton
#
# assert n > 0
#     top = 0
#     while n:
#         n, d = n // 10, n % 10
#         if _________:
#             _________ = __________
#        elif d == top:
#            unique = _________
#     return unique


def transitive(p):

    """Return whether p is transitive over non-negative single digit integers.
    >>> transitive(lambda x, y: x < y) # if a < b and b < c, then a < c
    True
    >>> transitive(lambda x, y: abs(x-y) == 1) # E.g., p(3, 4) and p(4, 5), but not p(3, 5)
    False
    """
    abc = 0
    while abc < 1000:
        a, b, c = abc // 100, (abc % 100) // 10, abc % 10
        if p(a, b) and p(b, c) and not p(a, c):
            return False
        abc = abc + 1
    return True

# Skeleton
# 
# abc = 0
# while abc < 1000:
#     a, b, c = abc // 100, __________, abc % 10
#     if p(a, b) __________:
#        return False
#     abc = abc + 1
# return True


def compose(n):

    """Return a function that, when called n times repeatedly on unary
    functions f1, f2, ..., fn, returns a function g(x) equivalent to
    f1(f2( ... fn(x) ... )).
    >>> add1 = lambda y: y + 1
    >>> compose(3)(abs)(add1)(add1)(-4) # abs(add1(add1(-4)))
    2
    >>> compose(3)(add1)(add1)(abs)(-4) # add1(add1(abs(-4)))
    6
    >>> compose(1)(abs)(-4) # abs(-4)
    4
    """
    assert n > 0
    if n == 1:
        return lambda f: f

    def call(f):
        def on(g):
            return compose(n-1)(lambda x: f(g(x)))
        return on
    return call

# Skeleton
#     assert n > 0
#     if n == 1:
#         return _________
# 
#     def call(f):
#         def on(g):
#             return ______(________)
#         return on
#     return call


from operator import add

"""Complete the final expression below with only integers and names so it evaluates to 2020"""

c = lambda f: lambda x: lambda y: f(x, y)
twice = lambda z: 2 * z

compose(3)(twice)(c(add)(10))(c(pow)(10))(3)    # 2 * (10 + (10^3)) = 2020

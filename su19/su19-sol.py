def compound(f):
    """Return a function that, when called the nth time, applies f repeatedly n times.
    >>> double = lambda y: 2 * y
    >>> doubler = compound(double)
    >>> doubler(3) # 1st call to doubler; double 3 one time
    6
    >>> doubler(5) # 2nd call to doubler; double 5 two times
    20
    >>> doubler(7) # 3rd call to doubler; double 7 three times
    56
    """
    h = lambda x: x

    def g(x):
        nonlocal h
        h = (lambda hh: lambda x: f(hh(x)))(h)
        return h(x)
    return g

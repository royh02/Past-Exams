
# Implement sequence, which takes a positive integer n and a function term. It returns an integer whose digits
# show the n elements of the sequence term(1), term(2), . . . , term(n) in order. Assume the term function takes
# a positive integer argument and returns a positive integer.
# Important: You may not use pow, **, log, str, or len in your solution.
def sequence(n, term):
    """Return the first n terms of a sequence as an integer.
    >>> sequence(6, abs) # Terms are 1, 2, 3, 4, 5, 6
    123456
    >>> sequence(5, lambda k: k+8) # Terms are 9, 10, 11, 12, 13
    910111213
    >>> sequence(4, lambda k: pow(10, k)) # Terms are 10, 100, 1000, 10000
    10100100010000
    """
    t, k = 0, 1
    while k <= n:
        m = 1
        x = term(k)
        while m <= x:
            m *= 10
        t = t * m + term(k)
        k = k + 1
    return t

# ORIGINAL SKELETON FOLLOWS

# # Implement sequence, which takes a positive integer n and a function term. It returns an integer whose digits
# # show the n elements of the sequence term(1), term(2), . . . , term(n) in order. Assume the term function takes
# # a positive integer argument and returns a positive integer.
# # Important: You may not use pow, **, log, str, or len in your solution.
# def sequence(n, term):
#     """Return the first n terms of a sequence as an integer.
#     >>> sequence(6, abs) # Terms are 1, 2, 3, 4, 5, 6
#     123456
#     >>> sequence(5, lambda k: k+8) # Terms are 9, 10, 11, 12, 13
#     910111213
#     >>> sequence(4, lambda k: pow(10, k)) # Terms are 10, 100, 1000, 10000
#     10100100010000
#     """
#     t, k = 0, 1
#     while ______:
#         m = 1
#         x = ______
#         while m <= x:
#             ______
#         t = ______
#         k = k + 1
#     return t


def announce_losses(who, last_score=0):
    """
    >>> f = announce_losses(0)
    >>> f1 = f(10, 0)
    >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
    Oh no! Player 0 just lost 9 point(s).
    >>> f3 = f2(7, 10)
    >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
    >>> f5 = f4(11, 12)
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'

    def say(score0, score1):
        if who == 0:
            score = score0
        elif who == 1:
            score = score1

        if last_score > score:
            print("Oh no! Player", who, "just lost",
                  last_score - score, "point(s)")
        return announce_losses(who, score)
    return say


def subset_sum(seq, k):
    """
    >>> subset_sum([2, 4, 7, 3], 5) # 2 + 3 = 5
    True
    >>> subset_sum([1, 9, 5, 7, 3], 2)
    False
    >>> subset_sum([1, 1, 5, -1], 3)
    False
    """
    if not seq:
        return False
    if k in seq:
        return True
    if seq[0] > k:
        return subset_sum(seq[1:], k)
    return subset_sum(seq[1:], k - seq[0])

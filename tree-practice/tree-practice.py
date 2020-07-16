# ################### burn the trees, they suck #######################

# still, i have to understand them to complete their eradication

def tree(label, branches=[]):
    return [label] + list(branches)


def is_leaf(t):
    return not branches(t)


def label(t):
    return t[0]


def branches(t):
    return t[1:]


def max_path(t, k):
    """ Return a list of the labels on any path in tree t of length at most k with the greatest sum
    >>> t1 = tree(6, [tree(3, [tree(8)]), tree(1, [tree(9), tree(3)])])
    >>> max_path(t1, 3)
    [6, 3, 8]
    >>> max_path(t1, 2)
    [3, 8]
    >>> t2 = tree(5, [t1, tree(7)])
    >>> max_path(t2, 1)
    [9]
    >>> max_path(t2, 2)
    [5, 7]
    >>> max_path(t2, 3)
    [6, 3, 8]
    """
    def helper(t, k, on_path):
        if k == 0:
            return []
        elif is_leaf(t):
            return [label(t)]
        a = [[label(t)] + helper(br, k-1, True) for br in branches(t)]
        if on_path:
            return max(a, key=sum)
        else:
            b = [helper(br, k, False) for br in branches(t)]
            return max(a + b, key=sum)
    return helper(t, k, False)


def is_combo(n, k):
    """Is k a combo of n?
    >>> [k for k in range(1000) if is_combo(357, k)]
    [0, 7, 12, 15, 22, 35, 56, 105]
    """
    assert n >= 0 and k >= 0
    if n == k or k == 0:
        return True
    if k != int(k) or n < k:
        return False
    rest, last = n // 10, n % 10
    added = k >= last and is_combo(rest, k - last)
    multiplied = k % last == 0 and is_combo(rest, k // last)
    return added or multiplied

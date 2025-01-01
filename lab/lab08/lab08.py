## Sets + Orders of Growth ##

# Q2
def find_duplicates(lst):
    """Returns True if lst has any duplicates and False if it does not.

    >>> find_duplicates([1, 2, 3, 4, 5])
    False
    >>> find_duplicates([1, 2, 3, 4, 2])
    True
    >>> find_duplicates(list(range(100000)) + [-1]) # make sure you have linear time
    False
    """
    a = set(lst)
    if len(a) == len(lst):
        return False
    return True


# Q3
def pow(n, k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    >>> a = pow(2, 100000000) # make sure you have log time
    """
    answer = n
    k -= 1
    while k > 0:
        if k % 2 == 0:
            answer = answer*answer
            k = k/2
        else:
            answer = answer*n
            k -= 1
    return answer

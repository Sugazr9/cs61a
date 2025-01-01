## Lab 6: OOP and Nonlocal ##

# Question 1
def vending_machine(snacks):
    """Cycles through list of snacks.
    
    >>> vender = vending_machine(['chips', 'chocolate', 'popcorn'])
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(['brownie'])
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    previous = len(snacks) - 1

    def item():
        nonlocal previous
        if previous == len(snacks) - 1:
            previous = 0
        else:
            previous += 1
        return snacks[previous]
    return item

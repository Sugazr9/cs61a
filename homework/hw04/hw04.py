###########
# Objects #
###########

# Q1

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    balance = 0
    stock = 0

    def __init__(self, item, cost):
        self.item = item
        self.cost = cost

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.balance < self.cost:
            return 'You must deposit $' + str(self.cost-self.balance) + ' more.'
        else:
            self.stock -= 1
            change = self.balance - self.cost
            self.balance = 0
            if change > 0:
                return 'Here is your ' + self.item + ' and $' + str(change) + ' change.'
            else:
                return 'Here is your ' + self.item + '.' 

    def restock(self, amount):
        self.stock += amount
        return 'Current ' + self.item + ' stock: ' + str(self.stock)

    def deposit(self, amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $' + str(amount) + '.'
        else:
            self.balance += amount
            return 'Current balance: $' + str(self.balance)


# Q2

class Interval:
    """A range of floating-point values.

    >>> a = Interval(1, 4)
    >>> a
    interval(1, 4)
    >>> print(a)
    (1, 4)
    >>> a.low
    1
    >>> a.high
    4
    >>> a.low = 3    # .low and .high are read-only
    AttributeError
    >>> a.width
    3
    >>> a.width = 4
    AttributeError
    >>> b = Interval(2, -2)  # Order doesn't matter
    >>> print(b, b.low, b.high)
    (-2, 2) -2 2
    >>> a + b
    interval(-1, 6)
    >>> a - b
    interval(-1, 6)
    >>> a * b
    interval(-8, 8)
    >>> b / a
    interval(-2.0, 2.0)
    >>> a / b
    ValueError
    >>> -a
    interval(-4, -1)
    """
    
    def __init__(self, a, b):
        self._low = min(a, b)
        self._high = max(a, b)

    @property
    def low(self):
        return self._low

    @property
    def high(self):
        return self._high

    def __str__(self):
        return '('+str(self.low)+', '+str(self.high)+')'

    def __repr__(self):
        return 'interval'+'('+str(self.low)+', '+str(self.high)+')'

    def __add__(self, other):
        if type(self) is type(other):
            return Interval((self.low + other.low), (self.high + other.high))

    def __sub__(self, other):
        if type(self) is type(other):
            return Interval((self.low - other.high), (self.high - other.low))

    def __mul__(self, other):
        if type(self) is type(other):
            min_value = self.low*other.high
            max_value = self.high*other.high
            for x in range(self.low, self.high+1):
                for y in range(other.low, other.high+1):
                    if min_value > x*y:
                        min_value = x*y
                    if max_value < x*y:
                        max_value = x*y
            return Interval(min_value, max_value)

    def __truediv__(self, other):
        if type(self) is type(other):
            min_value = self.low/other.high
            max_value = self.high/other.high
            for x in range(self.low, self.high+1):
                for y in range(other.low, other.high+1):
                    if y == 0:
                        raise ValueError("Division by interval containing 0")
                    if min_value > x/y:
                        min_value = x/y
                    if max_value < x/y:
                        max_value = x/y
            return Interval(min_value, max_value)

    def __neg__(self):
        if type(self) is Interval:
            return Interval(0 - self.high, 0 - self.low)

    @property
    def width(self):
        return self._high - self._low


# Q3

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, objct):
        self.object = objct

    def ask(self, command, *args):
        if command[:6] == 'please':
            command = command[7:]
            if hasattr(self.object, command):
                return getattr(self.object, command)(*args)
            else:
                return 'Thanks for asking, but I know not how to ' + command + '.'
        else:
            return 'You must learn to say please first.'


# Q4, Q5, and Q6

class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        >>> len(ints_list(100000)) # Check for iterative solution
        100000
        """
        length = 1
        end = self
        while end.rest is not Link.empty:
            length += 1
            end = end.rest
        return length

    # The following method may be useful for implementation of the
    # __getitem__ and insert methods.
    def _get_link(self, i):
        """An internal utility method that returns the Ith Link after
        self (I == 0 returns self, I == 1 returns self.rest, etc.).  Returns
        empty if I is len(self).  Raises IndexError unless 0 <= I <= len(self).
        >>> L = Link(1, Link(2, Link(3)))
        >>> L._get_link(0)
        Link(1, Link(2, Link(3)))
        >>> L._get_link(1)
        Link(2, Link(3))
        >>> L._get_link(2)
        Link(3)
        >>> L._get_link(3)
        ()
        >>> L._get_link(4)
        Traceback (most recent call last):
           ...
        IndexError: list index out of range
        >>> L._get_link(-1)
        Traceback (most recent call last):
           ...
        IndexError: list index out of range
        >>> (ints_list(100000))._get_link(1).first
        2
        """
        if i < 0:
            raise IndexError("list index out of range")
        target_link = self
        while i > 0:
            target_link = target_link.rest
            i -= 1
        return target_link

    def __getitem__(self, i):
        """Returns the element found at index I.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        >>> (ints_list(100000))[1]  # Check for iterative solution
        2
        """
        if i < 0:
            i = len(self) + i
        the_link = self._get_link(i)
        return the_link.first

    def __add__(self, lst):
        """Returns the result of non-destructively appending LST to the
        end of the sequence starting with self.
        """
        addition_link = lst
        for x in reversed(range(len(self))):
            addition_link = Link(self[x], addition_link)
        return addition_link

    def insert(self, k, val):
        """Destructively insert VAL into the list headed by SELF at index
        K, moving the previous item K and later items right.  Returns the
        resulting linked list.  Assumes 0 <= K <= len(self).
        """
        intermediate = Link(val) + self._get_link(k)
        for x in reversed(range(k)):
            intermediate = Link(self[x]) + intermediate
        self.first = intermediate.first
        self.rest = intermediate.rest
        return self


# ints_list is used to test that a method does not use recursion by making
# sure that a very long list does not cause a large recursion depth.
def ints_list(k):
    """A linked list containing the numbers 1 to K."""
    if k < 1:
        return Link.empty
    p = result = Link(1)
    for i in range(2, k + 1):
        p.rest = Link(i)
        p = p.rest
    return result


def add(L0, L1):
    """Return the list formed by non-destructively appending the items in L1
    to the end of those in L0.

    >>> s = Link(1, Link(2))
    >>> s + Link.empty
    Link(1, Link(2))
    >>> s + Link(3, Link(4))
    Link(1, Link(2, Link(3, Link(4))))
    >>> s   # Non-destructive
    Link(1, Link(2))
    >>> add(Link.empty, s)
    Link(1, Link(2))
    >>> s = ints_list(100000) + Link(100001)  # Check for iterative solution
    """
    if L0 is Link.empty:
        return L1
    else:
        return L0 + L1


def insert(L, k, val):
    """Destructively insert VAL into L at position K, returning the
    resulting list.  Assumes 0 <= K <= len(L).

    >>> L = Link(1, Link(2, Link(3)))
    >>> L.insert(1, 5)
    Link(1, Link(5, Link(2, Link(3))))
    >>> L
    Link(1, Link(5, Link(2, Link(3))))
    >>> L.insert(4, 6)  # Insert off the end.
    Link(1, Link(5, Link(2, Link(3, Link(6)))))
    >>> L.insert(0, 7)  # Insert at front
    Link(7, Link(1, Link(5, Link(2, Link(3, Link(6))))))
    >>> L  # New element is "left of" L
    Link(1, Link(5, Link(2, Link(3, Link(6)))))
    >>> L.insert(6, 8)
    IndexError
    >>> insert((), 0, 3)
    Link(3)
    """
    if L is Link.empty:
        L.first = val
        return L
    else:
        return L.insert(k, val)


class Tree:
    def __init__(self, label, children=()):
        self.label = label
        for branch in children:
            assert isinstance(branch, Tree)
        self.children = list(children)

    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.label, children_str)

    def is_leaf(self):
        return not self.children


# Q7

def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape iff they have the same number of children and each pair
    of corresponding children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = Tree(4, [Tree(7)])
    >>> same_shape(t, s)
    False
    """
    if t1.is_leaf and t2.is_leaf:
        return True
    if len(t1.children) == len(t2.children):
        for x in range(len(t1.children)):
            same_shape(t1.children[x], t2.children[x])
        return True
    return False


# Q8

def long_paths(tree, n):
    """Return a list all paths in tree with length at least n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12)])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    Link(0, Link(1, Link(2)))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    Link(0, Link(6, Link(9)))
    Link(0, Link(11, Link(12)))
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    >>> long_paths(whole, 4)
    []
    """
    if n == 0:
        return [Link(tree.label)]
    elif tree.is_leaf:
        return [Link.empty]
    return [Link(tree.label, long_paths(children, n-1)) for children in tree.children]

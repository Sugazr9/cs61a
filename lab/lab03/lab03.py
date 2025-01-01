from utils import *

# Q1
from math import sqrt


def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    x1 = get_lat(city1)
    x2 = get_lat(city2)
    y1 = get_lon(city1)
    y2 = get_lon(city2)
    distance = sqrt((x1-x2)**2 + (y1-y2)**2)

    return distance


# Q2
def closer_city(lat, lon, city1, city2):
    """ Returns the name of either city1 or city2, whichever is closest
        to coordinate (lat, lon).

        >>> berkeley = make_city('Berkeley', 37.87, 112.26)
        >>> stanford = make_city('Stanford', 34.05, 118.25)
        >>> closer_city(38.33, 121.44, berkeley, stanford)
        'Stanford'
        >>> bucharest = make_city('Bucharest', 44.43, 26.10)
        >>> vienna = make_city('Vienna', 48.20, 16.37)
        >>> closer_city(41.29, 174.78, bucharest, vienna)
        'Bucharest'
    """
    my_city = make_city('My Location', lat, lon)
    distance_city1 = distance(my_city, city1)
    distance_city2 = distance(my_city, city2)
    if distance_city1 < distance_city2:
        return get_name(city1)
    else:
        return get_name(city2)


# Q3
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    def multiplication(a, b, c, i=0):
        if b == 0:
            return i + c
        i += a
        return multiplication(a, b-1, c, i)
    if a == 0 or b == 0:
        product = 0
        return product + c
    solution = multiplication(a, b, c)
    return solution


# Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise. 

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def check_prime(n, factor=2):
        if factor == n:
            return True
        if n % factor == 0:
            return False
        if factor != n:
            return check_prime(n, factor + 1)
    if n == 1:
        return False
    if n < 4:
        return True
    return check_prime(n)


# Q5
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    def sum_odds(n, odd_term, k=1, total=0):
        if k > n:
            return total
        total += odd_term(k)
        return sum_odds(n, odd_term, k+2, total)

    def sum_evens(n, even_term, k=2, total=0):
        if k > n:
            return total
        total += even_term(k)
        return sum_evens(n, even_term, k+2, total)
    return sum_evens(n, even_term) + sum_odds(n, odd_term)
